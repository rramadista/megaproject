from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('banks', views.bank_list, name='bank_list'),
    path('branch', views.branch_list, name='branch_list'),
    path('orange', views.mount_orange_school, name='mount_orange_school'),
]