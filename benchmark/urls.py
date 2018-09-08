from django.urls import path
from .views import BankListView, BankDetailView, BankCreateView
from . import views

urlpatterns = [
    path('landing/', views.index, name='index'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reporting/', views.reporting, name='reporting'),
    path('analytics/', views.analytics, name='analytics'),
    # path('bank/', views.bank_list, name='bank_list'),
    # path('bank/add', views.bank_add, name='bank_add'),
    # path('bank/<int:pk>/', views.bank_detail, name='bank_detail'),
    path('bank/<int:pk>/edit/', views.bank_edit, name='bank_edit'),
    path('bank/<int:pk>/delete/', views.bank_delete, name='bank_delete'),
    path('branch/', views.branch_list, name='branch_list'),
    path('sample/', views.sample, name='sample'),

    # Class-Based View
    path('bank/', BankListView.as_view(), name='bank_list'),
    path('bank/<int:pk>/', BankDetailView.as_view(), name='bank_detail'),
    path('bank/new', BankCreateView.as_view(), name='bank_add'),
]
