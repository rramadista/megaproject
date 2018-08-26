from django import forms
from .models import Bank

OWNERSHIP = (
        ('1', 'Stated Owned Bank'),
        ('2', 'Regional Bank'),
        ('3', 'Private Forex Bank'),
        ('4', 'Private Non-Forex Bank'),
        ('5', 'Joint Venture Bank'),
        ('6', 'Foreign Bank'),
    )

class BankForm(forms.ModelForm):
    
    class Meta:
        model = Bank
        fields = ('institution_name', 'bank_name')

class RawBankForm(forms.Form):
    institution_name = forms.CharField(
        label='', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Institution Name"
                }
            )
        )
    bank_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bank Name"
                }
            )
        )
    est_date = forms.DateField(
        label='',
        widget=forms.DateInput(
            attrs={
                "placeholder": "Established Date",
                "class": "datepicker"
                }
            )
        )
    website = forms.URLField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Website"
                }
            )
        )
    category = forms.MultipleChoiceField(
        label='',
        widget=forms.Select(),
        choices=OWNERSHIP
        )
    logo = forms.ImageField(
        label='',
        widget=forms.ClearableFileInput(
            attrs={
                "class": "dropify",
                "data-height": "100",
                "data-show-loader": "false"
                }
            )
        )
