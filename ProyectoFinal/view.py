from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Depto.models import *
from Depto.forms import *

def home(request):
    dia = datetime.now()
    return render(request, "home.html")
    #return HttpResponse(f"Hola soy Brahian <br> <br> {dia}")

def about_me(request):
    return render(request, "aboutMe.html")

def about_pages(request):
    return render(request, "aboutPages.html")    

def contacto_request(request):
    return render(request, "contacto.html")   

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'inicio.html', {'avatar': avatar})
            else:
                return render(request, "perfiles/login.html", {'form':form})
        else:
            return render(request, "perfiles/login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, "perfiles/login.html", {'form':form})

def registro(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.changed_data["username"]
            form.save()
            return redirect("/Depto/inicio")
        else:
            return render(request, "perfiles/registro.html", {'form':form})
    
    form = UserRegisterForm()
    return render(request, "perfiles/registro.html", {'form':form})