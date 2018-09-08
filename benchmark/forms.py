from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Bank, Contact

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'dropify'}),
            'est_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        # labels = {'institution_name': '', 'bank_name': '', 'est_date': '', 'logo': ''}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'