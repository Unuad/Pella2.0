from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(reguest):
    return render(reguest, 'main/index.html')

def about(reguest):
    return render(reguest, 'main/about.html')
