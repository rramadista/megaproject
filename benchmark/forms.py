from django import forms
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bank, Contact, Indicator, Shareholder, Executive
from material import Layout, Fieldset, Row, Column, Span6, Span4, Span3, Span2


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
    # category = forms.ChoiceField(
    #     choices=Bank.OWNERSHIP,
    #     label='Bank Category',
    #     widget=forms.RadioSelect)
    # group = forms.ChoiceField(
    #     choices=Bank.BUKU, label='BUKU', widget=forms.RadioSelect)
    layout = Layout(
        Fieldset(
            "Institution Data", 'institution_name', 'bank_name',
            Row(
                Column('est_date', 'forex_date', 'listing_date'),
                Column('tin', 'logo'))),
        Fieldset("Bank Details", Row('category', 'group')))

    class Meta:
        model = Bank
        exclude = ['periods']
        widgets = {
            # 'logo': forms.FileInput(attrs={'class': 'dropify'}),
            'est_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'forex_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'listing_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class ContactForm(forms.ModelForm):
    layout = Layout(
        'bank',
        Fieldset("Bank Contacts", Row('phone', 'fax'), Row('email', 'website'),
                 Row('swift_code', 'contact_center')),
        Fieldset("Address", Row(
            Column('address_line', 'building_name'), 'city')))

    class Meta:
        model = Contact
        fields = '__all__'


class ShareholderForm(forms.ModelForm):
    layout = Layout(
        'bank',
        Fieldset("Shareholders", Row(Span4('shareholder'), Span2('share'), Span4('ultimate_country_name'), Span2('ultimate_country_id')),
                 Row(Span6('category'), Span6('is_ultimate'))))

    class Meta:
        model = Shareholder
        fields = '__all__'


class ExecutiveForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=Executive.GENDER,
        # label='Bank Category',
        widget=forms.RadioSelect)
    layout = Layout(
        Row(Span6('bank'), Span6('period')),
        Fieldset("Bank Executives",
                 Row(Span6('name'), Span2('gender'), Span4('photo')),
                 Row(Span6('title'), Span6('report_to')),
                 'is_current'))

    class Meta:
        model = Executive
        fields = '__all__'


class IndicatorForm(forms.ModelForm):
    pbt = forms.CharField()
    funding = forms.CharField()
    lending = forms.CharField()
    asset = forms.CharField()
    headcount = forms.CharField()
    layout = Layout(
        Row(Span6('bank'), Span6('period')),
        Fieldset("Bank Indicators", 
                 Row('pbt', 'asset', 'funding', 'lending'),
                 Row(Span6('is_current'), Span6('headcount'))))

    class Meta:
        model = Indicator
        fields = '__all__'

    def clean_name(self):
        # custom validation for the name field
        pass


BankIndicatorFormSet = inlineformset_factory(
    Bank,
    Indicator,
    fields=('period', 'asset'),
    extra=1,
    fk_name='bank',
    widgets={'period': forms.SelectDateWidget()})

IndicatorFormSet = inlineformset_factory(
    Bank,
    Indicator,
    form=IndicatorForm,
    extra=1,
    fk_name='bank',
    # can_order=True,
    can_delete=False,
    widgets={
        'period': forms.DateInput(attrs={'class': 'datepicker'}),
        # 'period': forms.SelectDateWidget(),
        'is_current': forms.CheckboxInput()
    })

# IndicatorFormSet = modelformset_factory(
#     Indicator,
#     form=IndicatorForm,
#     widgets={
#         'period': forms.DateInput(attrs={'class': 'datepicker'}),
#     })
