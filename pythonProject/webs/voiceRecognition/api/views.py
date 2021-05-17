from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Browse this portal properly')

# Create your views here.
