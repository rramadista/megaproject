from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Bank, Contact

class BankModelForm(forms.ModelForm):
    # institution_name = forms.CharField(
    #     label='INSTITUTION NAME',
    #     widget=forms.TextInput(attrs={"placeholder": "Institution Name"}))
    # bank_name = forms.CharField(
    #     label='BANK NAME', widget=forms.TextInput(attrs={"placeholder": "Bank Name"}))
    # est_date = forms.DateField(
    #     label='ESTABLISHED DATE',
    #     widget=forms.DateInput(attrs={
    #         "placeholder": "Established Date",
    #         "class": "datepicker"
    #     }))

    class Meta:
        model = Bank
        fields = ('institution_name', 'bank_name', 'est_date', 'logo')
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'dropify'}),
            'est_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }


    def clean_title(self, *args, **kwargs):
        institution_name = self.cleaned_data.get("institution_name")
        if not "Bank" in institution_name:
            raise forms.ValidationError("This is not a valid institution")
        return institution_name

class BankForm(forms.Form):
    institution_name = forms.CharField(
        label='INSTITUTION NAME',
        widget=forms.TextInput(attrs={"placeholder": "Institution Name"}))
    bank_name = forms.CharField(
        label='BANK NAME', widget=forms.TextInput(attrs={"placeholder": "Bank Name"}))
    est_date = forms.DateField(
        label='ESTABLISHED DATE',
        widget=forms.DateInput(attrs={
            "placeholder": "Established Date",
            "class": "datepicker"
        }),
        help_text="pick a date")
    # category = forms.MultipleChoiceField(
    #     label='CATEGORY', widget=forms.Select(), choices=OWNERSHIP)
    # logo = forms.ImageField(
    #     label='LOGO',
    #     widget=forms.ClearableFileInput(attrs={
    #         "class": "dropify",
    #         "data-height": "100",
    #         "data-show-loader": "false"
    #     }))

class ContactForm(forms.Form):
    building_name = forms.CharField(
        label='BUILDING NAME',
        widget=forms.TextInput(attrs={"placeholder": "Building Name"}))
    website = forms.URLField(
        label='WEBSITE', widget=forms.TextInput(attrs={"placeholder": "Website"}))