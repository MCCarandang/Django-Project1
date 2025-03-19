# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse
    return render(request, 'home.html')     #naka link sa settings.py

def about(request):
    # return HttpResponse
    return render(request, 'about.html')        #naka link sa settings.py
