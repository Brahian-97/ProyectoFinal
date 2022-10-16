from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from Depto.models import *
from Depto.forms import form_integrantes, form_GastosFijos, form_GastosDiarios

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    return render(request, "inicio.html")

def gastos(request):
    return render(request, 'gastos.html')

#GASTOS FIJOS

def gastosFijos(request):
    return render(request, 'gastosFijos.html')

def create_fijos(request):
    if request.method == 'POST':
        gastosF = GastosFijos(nombre = request.POST['nombre'], tipo = request.POST['tipo'], valor = request.POST['valor'], fechaDeVencimiento = request.POST['fechaDeVencimiento'])
        gastosF.save()
        gastosF = GastosFijos.objects.all()
        return render(request, "gastosCRUD/read_gastosF.html", {"gastosF": gastosF})
    return render(request, "gastosCRUD/create_gastosF.html")

def read_fijos(request):
    gastosF = GastosFijos.objects.all() #trae todo
    return render(request, "gastosCRUD/read_gastosF.html", {"gastosF": gastosF})

def update_fijos(request, gastoF_id):
    gastoF = GastosFijos.objects.get(id = gastoF_id)

    if request.method == 'POST':
        formulario = form_GastosFijos(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            gastoF.nombre = informacion['nombre']
            gastoF.tipo = informacion['tipo']
            gastoF.valor = informacion['valor']
            gastoF.fechaDeVencimiento = informacion['fechaDeVencimiento']
            gastoF.save()
            gastosF = GastosFijos.objects.all() #trae todo
            return render(request, "gastosCRUD/read_gastosF.html", {"gastosF": gastosF})
    else:
        formulario = form_GastosFijos(initial={'nombre': gastoF.nombre,'tipo': gastoF.tipo,'valor': gastoF.valor, 'fechaDeVencimiento': gastoF.fechaDeVencimiento})
    return render(request, "gastosCRUD/update_gastosF.html", {"formulario": formulario})

def delete_fijos(request, gastoF_id):
    gastoF_id = GastosFijos.objects.get(id = gastoF_id)
    gastoF_id.delete()
    gastosF = GastosFijos.objects.all()
    return render(request, "gastosCRUD/read_gastosF.html", {"gastosF": gastosF})

def buscar_fijos(request):
    if request.GET["fechaDeVencimiento"]:
        fechaDeVencimiento = request.GET["fechaDeVencimiento"]
        gastosF = GastosFijos.objects.filter(fechaDeVencimiento__icontains = fechaDeVencimiento)
        return render(request, "gastosFijos.html", {"gastosF": gastosF})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#GASTOS DIARIOS

def gastosDiarios(request):
    return render(request, 'gastosDiarios.html')

def create_diarios(request):
    if request.method == 'POST':
        gastosD = GastosDiarios(nombre = request.POST['nombre'], tipo = request.POST['tipo'], valor = request.POST['valor'], fecha = request.POST['fecha'])
        gastosD.save()
        gastosD = GastosDiarios.objects.all()
        return render(request, "gastosCRUD/read_gastosD.html", {"gastosD": gastosD})
    return render(request, "gastosCRUD/create_gastosD.html")

def read_diarios(request):
    gastosD = GastosDiarios.objects.all() #trae todo
    return render(request, "gastosCRUD/read_gastosD.html", {"gastosD": gastosD})

def update_diarios(request, gastoD_id):
    gastoD = GastosDiarios.objects.get(id = gastoD_id)

    if request.method == 'POST':
        formulario = form_GastosDiarios(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            gastoD.nombre = informacion['nombre']
            gastoD.tipo = informacion['tipo']
            gastoD.valor = informacion['valor']
            gastoD.fecha = informacion['fecha']
            gastoD.save()
            gastosD = GastosDiarios.objects.all() #trae todo
            return render(request, "gastosCRUD/read_gastosD.html", {"gastosD": gastosD})
    else:
        formulario = form_GastosDiarios(initial={'nombre': gastoD.nombre,'tipo': gastoD.tipo,'valor': gastoD.valor, 'fecha': gastoD.fecha})
    return render(request, "gastosCRUD/update_gastosD.html", {"formulario": formulario})

def delete_diarios(request, gastoD_id):
    gastoD_id = GastosDiarios.objects.get(id = gastoD_id)
    gastoD_id.delete()
    gastosD = GastosDiarios.objects.all()
    return render(request, "gastosCRUD/read_gastosD.html", {"gastosD": gastosD})

def buscar_diarios(request):
    if request.GET["fecha"]:
        fecha = request.GET["fecha"]
        gastosD = GastosDiarios.objects.filter(fecha__icontains = fecha)
        return render(request, "gastosDiarios.html", {"gastosD": gastosD})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#INTEGRANTES

@login_required
def integrantes(request):
    if request.method == "POST":
        integrante = Integrantes(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'], depto = request.POST['depto'])
        integrante.save()
        #avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request, 'inicio.html', {'avatar': avatar})
    return render(request, "integrantes.html")

def create_integrantes(request):
    if request.method == 'POST':
        integrantes = Integrantes(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'], depto = request.POST['depto'])
        integrantes.save()
        integrantes = Integrantes.objects.all()
        return render(request, "integrantesCRUD/read_integrantes.html", {"integrantes": integrantes})
    return render(request, "integrantesCRUD/create_integrantes.html")

def read_integrantes(request):
    integrantes = Integrantes.objects.all() #trae todo
    return render(request, "integrantesCRUD/read_integrantes.html", {"integrantes": integrantes})
    

def update_integrantes(request, integrante_id):
    integrante = Integrantes.objects.get(id = integrante_id)

    if request.method == 'POST':
        formulario = form_integrantes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            integrante.nombre = informacion['nombre']
            integrante.apellido = informacion['apellido']
            integrante.email = informacion['email']
            integrante.depto = informacion['depto']
            integrante.save()
            integrantes = Integrantes.objects.all() #trae todo
            return render(request, "integrantesCRUD/read_integrantes.html", {"integrantes": integrantes})
    else:
        formulario = form_integrantes(initial={'nombre': integrante.nombre,'apellido': integrante.apellido,'email': integrante.email, 'depto': integrante.depto})
    return render(request, "integrantesCRUD/update_integrantes.html", {"formulario": formulario})
     

def delete_integrantes(request, integrante_id):
    integrante = Integrantes.objects.get(id = integrante_id)
    integrante.delete()
    integrantes = Integrantes.objects.all()
    return render(request, "integrantesCRUD/read_integrantes.html", {"integrantes": integrantes}) 

def buscar_integrantes(request):
    if request.GET["email"]:
        email = request.GET["email"]
        integrantes = Integrantes.objects.filter(email__icontains = email)
        return render(request, "integrantes.html", {"integrantes": integrantes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#TAREAS

def tareas(request):
    return render(request, "tareas.html")


#LOGIN

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                #avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'inicio.html', {'avatar': avatar})
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})
#
#def registro(request):
#    if request.method == 'POST':
#        #form = UserCreationForm(request.POST)
#        form = UserRegisterForm(request.POST)
#        if form.is_valid():
#            #username = form.changed_data["username"]
#            form.save()
#            return redirect("/AppCoder/login")
#        else:
#            return render(request, "registro.html", {'form':form})
#    
#    form = UserRegisterForm()
#    return render(request, "registro.html", {'form':form})