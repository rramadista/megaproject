from django import forms
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bank, Contact, Indicator
from material import Layout, Fieldset, Row, Column, Span


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
    category = forms.ChoiceField(
        choices=Bank.OWNERSHIP,
        label='Bank Category',
        widget=forms.RadioSelect)
    group = forms.ChoiceField(
        choices=Bank.BUKU, label='BUKU', widget=forms.RadioSelect)
    layout = Layout(
        Fieldset(
            "Institution Data", 'institution_name', 'bank_name',
            Row(
                Column('est_date', 'forex_date', 'listing_date'),
                Column('tin', 'logo'))),
        Fieldset("Bank Details", Row('category', 'group')),
        Fieldset("Indicators"))

    class Meta:
        model = Bank
        # fields = '__all__'
        exclude = ['periods']
        widgets = {
            # 'logo': forms.FileInput(attrs={'class': 'dropify'}),
            'est_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'forex_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'listing_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        # fields = ['pbt', 'asset', 'headcount']
        fields = '__all__'

    def clean_name(self):
        # custom validation for the name field
        pass


BankIndicatorFormSet = inlineformset_factory(
    Bank,
    Indicator,
    fields=(
        'period',
        'asset',
    ),
    extra=1,
    fk_name='bank',
    widgets={
        'period': forms.SelectDateWidget(),
    })

BankFormSet = modelformset_factory(
    Indicator,
    form=IndicatorForm,
    formset=BankIndicatorFormSet,
    widgets={
        'period': forms.DateInput(attrs={'class': 'datepicker'}),
    })
