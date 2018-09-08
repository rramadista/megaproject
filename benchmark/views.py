from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Bank, Contact, Indicator
from .forms import BankForm, ContactForm

# USER VIEWS
def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

# MENU VIEWS
def index(request):
    context = {}
    return render(request, 'general/index.html', context)

def home(request):
    context = {}
    return render(request, 'benchmark/home.html', context)

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
class BankListView(ListView):
    model = Bank
    template_name = 'benchmark/bank_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'banks'
    ordering = ['bank_name']

class BankDetailView(DetailView):
    model = Bank
    
class BankCreateView(CreateView):
    model = Bank
    fields = ['institution_name', 'bank_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def bank_list(request):
    banks = Bank.objects.all()
    context = {'banks': banks}
    return render(request, 'benchmark/bank_list.html', context)

def bank_detail(request, pk=None):
    bank = get_object_or_404(Bank, pk=pk)
    context = {'bank': bank}
    return render(request, 'benchmark/bank_detail.html', context)

def bank_add(request):
    # bank_form = BankForm(request.POST or None)
    # if bank_form.is_valid():
    #     bank = bank_form.save(commit=False)
    #     bank.save()
    #     bank_form = BankForm()

    if request.POST:
        bank_form = BankForm(request.POST)
        if bank_form.is_valid():
            bank_form.save()

            return HttpResponseRedirect('benchmark/bank_list.html')
        else:
            bank_form = BankForm()

    context = {'bank_form': bank_form}
    return render(request, 'benchmark/bank_edit.html', context)

def bank_edit(request, pk=None):
    bank = get_object_or_404(Bank, pk=pk)
    bank_form = BankForm(request.POST or None, instance=bank)
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