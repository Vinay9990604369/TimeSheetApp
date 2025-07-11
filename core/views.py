# core/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to TimeSheetApp! You are logged in." if request.user.is_authenticated else "Welcome! Please log in.")
