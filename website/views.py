from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

def index(request):
    return HttpResponse("<h1>Website Index</h1>")