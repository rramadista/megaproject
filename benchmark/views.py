from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Bank, Contact, Indicator
from .forms import BankForm, ContactForm, BankModelForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'benchmark/index.html', context)

def dashboard(request):
    context = {}
    return render(request, 'benchmark/dashboard.html', context)

def reporting(request):
    context = {}
    return render(request, 'benchmark/reporting.html', context)

def analytics(request):
    context = {}
    return render(request, 'benchmark/analytics.html', context)

# BANK VIEWS
def bank_list(request):
    banks = Bank.objects.all()
    context = {'banks': banks}
    return render(request, 'benchmark/bank_list.html', context)

def bank_detail(request, pk=None):
    bank = get_object_or_404(Bank, pk=pk)
    context = {'bank': bank}
    return render(request, 'benchmark/bank_detail.html', context)

def bank_add(request):
    bank_form = BankModelForm(request.POST or None)
    if bank_form.is_valid():
        bank_form.save()
        bank_form = BankModelForm()

    context = {'bank_form': bank_form}
    return render(request, 'benchmark/bank_edit.html', context)

def bank_edit(request, pk=None):
    # bank = get_object_or_404(Bank, pk=pk)
    # initial = vars(bank)
    # bank_form = BankForm(initial=initial)
    # if request.method == "POST":
    #     bank_form = BankForm(request.POST)
    #     if bank_form.is_valid():
    #         print(bank_form.cleaned_data)
    #     else:
    #         print(bank_form.errors)
    # bank_form = BankForm()

    # bank = get_object_or_404(Bank, pk=pk)
    # initial = vars(bank)
    # bank_form = BankForm(initial=initial)
    # if request.method == "POST":
    #     bank_form = BankModelForm(request.POST, initial=initial, instance=bank)
    #     if bank_form.is_valid():
    #         bank_form.save()
    #         return redirect('bank_detail', pk=bank.pk)
    # else:
    #     bank_form = BankModelForm()

    bank = get_object_or_404(Bank, pk=pk)
    bank_form = BankModelForm(request.POST or None, instance=bank)
    if bank_form.is_valid():
        bank = bank_form.save(commit=False)
        bank.save()
        return redirect('bank_detail', pk=bank.pk)

    context = {'bank_form': bank_form, 'bank': bank}
    return render(request, 'benchmark/bank_edit.html', context)

def bank_delete(request, pk=None):
    bank = get_object_or_404(Bank, pk=pk)
    bank.delete()
    return redirect('bank_list')

# BRANCH VIEWS
def branch_list(request):
    return render(request, 'benchmark/branch_list.html', {})

def sample(request):
    return render(request, 'benchmark/sample.html', {})