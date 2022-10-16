from dataclasses import field, fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_integrantes(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    depto = forms.CharField(max_length=30)

class form_GastosFijos(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    valor = forms.IntegerField()
    fechaDeVencimiento = forms.DateField()

class form_GastosDiarios(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    valor = forms.IntegerField()
    fecha = forms.DateField()