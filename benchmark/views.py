from django.utils import timezone
from django.db import transaction
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages  # [debug/info/success/warning/error]
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Bank, Contact, Indicator
from .forms import BankForm, ContactForm, UserRegisterForm, BankIndicatorFormSet, IndicatorFormSet


# USER VIEWS
class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            # if user is not None:
            if user.exist():
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
    template_name = 'benchmark/bank_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'banks'
    ordering = ['-bank_name']  # descending


class BankDetailView(DetailView):
    model = Bank


class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    form_class = BankForm
    success_url = reverse_lazy('bank_list')

    def get_context_data(self, **kwargs):
        data = super(BankCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['bankindicators'] = IndicatorFormSet(self.request.POST)
        else:
            data['bankindicators'] = IndicatorFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        bankindicators = context['bankindicators']
        with transaction.atomic():
            self.object = form.save()
        if bankindicators.is_valid():
            bankindicators.instance = self.object
            bankindicators.save()

        return super(BankCreateView, self).form_valid(form)


class BankUpdateView(LoginRequiredMixin, UpdateView):
    model = Bank
    form_class = BankForm


class BankDeleteView(LoginRequiredMixin, DeleteView):
    model = Bank
    success_url = reverse_lazy('bank_list')


# BRANCH VIEWS
def branch_list(request):
    return render(request, 'benchmark/branch_list.html', {})


def sample(request):
    return render(request, 'benchmark/sample.html', {})