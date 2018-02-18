# Python/Django/website/music/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the Music homepage</h1>")
