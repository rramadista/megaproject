from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bank, Contact
from material import Layout, Fieldset, Row


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    layout = Layout(
        'username', 'email', Row('password1', 'password2'),
        Fieldset('Pesonal Details', Row('first_name', 'last_name')))

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'first_name',
            'last_name'
        ]


class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        # fields = '__all__'
        exclude = ['periods']
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'dropify'}),
            'est_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'