from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    BankListView, BankDetailView, BankCreateView, BankUpdateView, BankDeleteView, 
    BankContactCreateView, BankIndicatorCreateView, BankShareholderCreateView,
    BankExecutiveCreateView, UserFormView
)
from . import views

urlpatterns = [
    # Function-Based View
    path('landing/', views.index, name='index'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reporting/', views.reporting, name='reporting'),
    path('analytics/', views.analytics, name='analytics'),
    path('branch/', views.branch_list, name='branch_list'),
    path('sample/', views.sample, name='sample'),

    # Class-Based View
    path('register/', UserFormView.as_view(), name='register'),
    path('bank/', BankListView.as_view(), name='bank_list'),
    path('bank/<int:pk>/', BankDetailView.as_view(), name='bank_detail'),
    path('bank/add', BankCreateView.as_view(), name='bank_add'),
    path('bank/indicator/add', BankIndicatorCreateView.as_view(), name='bank_indicator_add'),
    path('bank/contact/add', BankContactCreateView.as_view(), name='bank_contact_add'),
    path('bank/shareholder/add', BankShareholderCreateView.as_view(), name='bank_shareholder_add'),
    path('bank/executive/add', BankExecutiveCreateView.as_view(), name='bank_executive_add'),
    path('bank/<int:pk>/edit/', BankUpdateView.as_view(), name='bank_edit'),
    path('bank/<int:pk>/delete/', BankDeleteView.as_view(), name='bank_delete'),
]
