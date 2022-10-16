from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

def home(request):
    dia = datetime.now()
    return render(request, "home.html")
    #return HttpResponse(f"Hola soy Brahian <br> <br> {dia}")
    


