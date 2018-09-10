from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages # [debug/info/success/warning/error]
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Bank, Contact, Indicator
from .forms import BankForm, ContactForm, UserForm, UserRegisterForm

# USER VIEWS
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {{ username }}!')
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

class UserFormView(View):
    form_class = UserRegisterForm
    # form_class = UserCreationForm
    # form_class = UserForm
    template_name = 'users/registration_form.html'
    # template_name = 'users/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})

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
    form_class = BankForm
    # fields = ['institution_name', 'bank_name']
    
class BankUpdateView(UpdateView):
    model = Bank
    fields = ['institution_name', 'bank_name', 'logo']

class BankDeleteView(DeleteView):
    model = Bank
    success_url = reverse_lazy('bank_list')

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