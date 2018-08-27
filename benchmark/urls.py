from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reporting/', views.reporting, name='reporting'),
    path('analytics/', views.analytics, name='analytics'),
    path('bank/', views.bank_list, name='bank_list'),
    path('bank/new', views.bank_new, name='bank_new'),
    path('bank/<int:pk>/', views.bank_detail, name='bank_detail'),
    path('bank/<int:pk>/edit/', views.bank_edit, name='bank_edit'),
    path('branch/', views.branch_list, name='branch_list'),
    path('sample/', views.sample, name='sample'),
]