from django.db.models.aggregates import Min
from payment.models import Payment
from django.contrib import messages
from new_door.models import TenantDocument, Unit
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import stripe

# stripe.api_key = config('STRIPE_SECRET_KEY')
stripe.api_key = 'sk_test_51I0mEFGz8qAcurV0PCi7DH9LM4fx9QghxgAxnV9eWAP1gmllKeSzmSIbDvU0THz6i0HzP7EdXHxBTVtbo1HHYd8u00lnHS3VYg'


# Create your views here.

@login_required
def payment(request, user):
    tenant_contract = ''
    property_owner = ''
    amount_remained = ''
    unit = ''
    profile = Profile.objects.get(user__username=user)
    user_docs = TenantDocument.objects.filter(tenant__user__username=user)

    try:
        tenant_contract = TenantContract.objects.get(
            tenant__user__username=user)

        unit = Unit.objects.filter(tenantcontract=tenant_contract).first()
        print(unit)

        property_owner = Property.objects.get(
            pk=tenant_contract.property_id_id)
    except TenantContract.DoesNotExist:
        messages.info(
            request, 'You dont have a contract to make payments for, please contact your real estate manager')
        return redirect('tenant_dashboard')

    if user_docs.count() == 0:
        messages.info(
            request, f"Please upload your documents")
        return redirect('tenant_dashboard')

    if not user_docs[0].is_verified:
        messages.info(
            request, f"Waiting for your documents to be verified")
        return redirect('tenant_dashboard')

    if tenant_contract.security_dep == None and tenant_contract.commission == None:
        messages.info(
            request, f"Sorry, you don't have a contract generated yet")
        return redirect('tenant_dashboard')

    # get variables
    unit_amount = TenantContract.objects.get(
        tenant__user__username=user).unit.rent_amount

    security_dep = TenantContract.objects.get(
        tenant__user__username=user).security_dep
    commission = TenantContract.objects.get(
        tenant__user__username=user).commission
    installment = TenantContract.objects.get(
        tenant__user__username=user).installments
    discount = TenantContract.objects.get(
        tenant__user__username=user).discount

    # get full amount
    final_amount = int(security_dep) + int(commission) + \
        int(unit_amount) - int(discount)

    # get min due amount
    try:
        amount_remained = Payment.objects.filter(
            contract=tenant_contract).aggregate(amount_remained=Min('remain_amount'))
        expire_month = installment // 12
    except:
        pass

    if request.method == "POST":
        # Check if email and card name are provided
        tenant_email = profile.user.email
        email = request.POST.get('email')
        card_name = request.POST.get('fullname')

        if email != tenant_email:
            messages.error(
                request, 'Make sure your is email and card name valid, this is due to mismatch of emails')
            return redirect("payment", user)

        if email == '' and card_name == '':
            messages.error(
                request, 'Make sure your email and card name are filled')
            return redirect("payment", user)

        # check if full payment is done
        try:
            payments = Payment.objects.filter(contract=tenant_contract)
            expire_month = installment // 12
            for payment in payments:

                if payment.remain_amount == 0:
                    messages.success(request, 'Payment completed')
                    return redirect("payment", user)
        except:
            pass

        # No charge at 0
        try:
            payments = Payment.objects.filter(contract=tenant_contract)

            for payment in payments:

                if payment.remain_amount == 0:
                    messages.success(request, 'Payment completed')
                    return redirect("payment", user)
        except:
            pass

        customer = stripe.Customer.create(
            name=card_name,
            email=email,
            source=request.POST.get('stripeToken')
        )
        rental_amount = stripe.Charge.create(
            customer=customer,
            amount=round(int(final_amount) * 100 / int(installment)),
            currency="usd",
            receipt_email=request.POST.get('email'),
        )

        if rental_amount.paid:
            unit_contract = Unit.objects.get(tenantcontract__tenant=profile)
            occupancy = OccupancyType.objects.get(
                occupancy_type__iexact="Occupied")
            # occupancy = OccupancyType.objects.get(
            #     occupancy_type__iexact="Create Contract")
            unit_contract.occupancy_type = occupancy
            unit_contract.save()

            messages.success(
                request, f'Payment of ${round(rental_amount.amount / 100)} has been made successfully')
            paid_amount = round(rental_amount.amount / 100)
            remain_amount = round(int(final_amount) - paid_amount)

            try:
                payments = Payment.objects.filter(contract=tenant_contract)
                for payment in payments:
                    r_amount = payment.remain_amount
                    p_amount = payment.amount
                    remain_amount = r_amount - p_amount

                Payment.objects.create(
                    contract=tenant_contract,
                    unit=unit,
                    amount=paid_amount,
                    status='Completed',
                    remain_amount=remain_amount,
                    remarks='Paid'
                )
            except Payment.DoesNotExist:
                intial_payment = Payment(
                    contract=tenant_contract,
                    amount=paid_amount,
                    status='Completed',
                    remain_amount=remain_amount,
                    remarks='Paid'
                )
                intial_payment.save()

                # print(intial_payment.amount)
                # if intial_payment.remain_amount == 0:
                #     messages.info(request, 'Payment completed')

            tenant_msg_success = f"Hi { user }, \n You have made a payment of ${ round(rental_amount.amount / 100) } to new door real estate \n your next payment is due on 3 March 2021"
            owner_msg_success = f"Hi { property_owner.owner_name.user.username }, \n { user.capitalize() } has made a payment of ${ rental_amount.amount // 100 } to unit flat number {unit_contract.flat}. \n next payment is due on 3 March 2021"

            send_mail(
                f'Payment Done for unit flat number {unit_contract.flat}',
                tenant_msg_success,
                'noreply@newdoor.com',
                [profile.user.email],
                fail_silently=False,
            )

            if property_owner.owner_name.user.email:
                send_mail(
                    f'Payment Done for unit flat number {unit_contract.flat}',
                    owner_msg_success,
                    'noreply@newdoor.com',
                    [property_owner.owner_name.user.email],
                    fail_silently=False,
                )
            else:
                pass

            return redirect('payment', profile.user.username)

        else:
            messages.error(
                request, 'There was a problem  making your payment make sure you details are correct')

    context = {
        'final_amount': round(final_amount / int(installment)),
        'amount_remained': amount_remained,
    }

    return render(request, 'payment/payment.html', context)


@login_required
def checklist(request):
    return render(request, 'new_door/checklist.html')