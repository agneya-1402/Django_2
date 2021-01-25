from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def exp(requests):
    return render(requests,'app1/index.html')