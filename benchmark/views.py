from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # return  HttpResponse("Hello World!")
    return render(request, 'benchmark/chart.html', {})