from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Bank, Indicator
from .forms import BankForm, BankModelForm

# Create your views here.
def index(request):
    return render(request, 'benchmark/index.html', {})

def dashboard(request):
    return render(request, 'benchmark/dashboard.html', {})

def reporting(request):
    return render(request, 'benchmark/reporting.html', {})

def analytics(request):
    return render(request, 'benchmark/analytics.html', {})

# BANK VIEWS
def bank_list(request):
    # banks = Bank.objects.order_by('-bank_name')
    banks = Bank.objects.all()
    return render(request, 'benchmark/bank_list.html', {'banks': banks})

def bank_detail(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    return render(request, 'benchmark/bank_detail.html', {'bank': bank})

def bank_new(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            # Bank.objects.create(form.cleaned_data)
            return redirect('bank_list')
    else:
        form = BankForm()
    return render(request, 'benchmark/bank_edit.html', {'form': form})

def bank_edit(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    # bank = request.GET.get(Bank, pk=pk)
    # queryset = Bank.objects.all()
    # form = BankForm(request.POST, initial=bank)
    initial = vars(bank)
    # form = BankForm(initial={'bank_name': 'Bank Karman'})
    form = BankForm(initial=initial)
    return render(request, 'benchmark/bank_edit.html', {'form': form})

# BRANCH VIEWS
def branch_list(request):
    return render(request, 'benchmark/branch_list.html', {})

def sample(request):
    return render(request, 'benchmark/sample.html', {})