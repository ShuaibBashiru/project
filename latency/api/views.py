from django.shortcuts import render
from django.http import HttpResponse
from scipy.optimize import linprog
# Create your views here.
def index(request):
    return HttpResponse("ho welcome")



