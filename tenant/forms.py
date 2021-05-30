from django import forms
from tenant.models import TenantContract
import datetime


class TenantContractModelForm(forms.ModelForm):
    remark = forms.CharField(
        widget=forms.TextInput(attrs={"col": "3", "row": "1", 'class': 'form-control'}))
    discount = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    annual_rent = forms.CharField(max_length=100,
                                  widget=forms.NumberInput(attrs={'class': 'form-control', "readonly": True}), required=False)
    security_dep = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    commission = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    installments = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = TenantContract
        fields = '__all__'
        exclude = ['id']

        widgets = {
            'tenant': forms.TextInput(attrs={'class': 'form-control', "readonly": True}),
            'property_id': forms.TextInput(attrs={'class': 'form-control', "readonly": True}),
            'unit': forms.TextInput(attrs={'class': 'form-control', "readonly": True}),
            'contract_no': forms.TextInput(attrs={'class': 'form-control', "readonly": True}),
            'sms_notify': forms.CheckboxInput(attrs={'class': 'form-check-input', "id": "sms_notify"},),
            'email_notify': forms.CheckboxInput(attrs={'class': 'form-check-input', "id": "email_notify"}),
        }

    def clean(self):
        clearned_data = super().clean()
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        # num_months = (end_date.year - start_date.year) * \
        #     12 + (end_date.month - start_date.month)

        # print("This is the diff", num_months)
        if end_date < start_date:
            self.add_error(
                'end_date', 'End Date should not less than Start date')
            raise forms.ValidationError(
                'End Date should not less than Start date')

        # elif (num_months < 12):
        #     self.add_error('end_date', 'Duration should be one year minimum')
        #     raise forms.ValidationError('Duration should be one year minimum')

        return clearned_data

    def clean_discount(self):
        discount = self.cleaned_data['discount']
        if discount.isnumeric() is not True:
            raise forms.ValidationError(
                'Discount should be in numeric character')
        return discount

    def clean_annual_rent(self):
        annual_rent = self.cleaned_data['annual_rent']
        if annual_rent.isnumeric() is not True:
            raise forms.ValidationError(
                'Annual Rent should be in numeric character')
        return annual_rent

    def clean_security_dep(self):
        security_dep = self.cleaned_data['security_dep']
        if security_dep.isnumeric() is not True:
            raise forms.ValidationError(
                'Security Deposit should be in numeric character')
        return security_dep

    def clean_commission(self):
        commission = self.cleaned_data['commission']
        if commission.isnumeric() is not True:
            raise forms.ValidationError(
                'Commission should be in numeric character')
        return commission

    def clean_installments(self):
        installments = self.cleaned_data['installments']
        if installments.isnumeric() is not True:
            raise forms.ValidationError(
                'Installments should be in numeric character')
        return installments

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        today = datetime.date.today()

        if start_date < today:
            self.add_error(
                'start_date', 'Start date should not be less than current date')
        return start_date


