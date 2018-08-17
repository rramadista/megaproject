from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Bank, Indicator

# Create your views here.
def index(request):
    return render(request, 'benchmark/index.html', {})

def dashboard(request):
    return render(request, 'benchmark/dashboard.html', {})

def reporting(request):
    return render(request, 'benchmark/reporting.html', {})

def analytics(request):
    return render(request, 'benchmark/analytics.html', {})

def bank_list(request):
    banks = Bank.objects.order_by('-bank_name')
    return render(request, 'benchmark/bank_list.html', {'banks': banks})

def bank_detail(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    return render(request, 'benchmark/bank_detail.html', {'bank': bank})

def branch_list(request):
    return render(request, 'benchmark/branch_list.html', {})

def sample(request):
    return render(request, 'benchmark/sample.html', {})