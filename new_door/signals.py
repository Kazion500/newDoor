
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Unit, TenantContract


@receiver(post_save, sender=User)
def post_save_end_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()


@receiver(post_save, sender=TenantContract)
def post_save_tenant_contract(sender, instance, created, **kwargs):
    if created:
        unit = Unit.objects.get(pk=instance.unit.pk)
        if instance.discount != None and instance.security_dep != None and instance.commission != None:
            annual_amount = instance.security_dep + instance.commission - instance.discount
            unit.rent_amount += annual_amount
            unit.save()


# instance.profile.save()
