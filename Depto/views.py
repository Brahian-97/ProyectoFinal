from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Depto.models import *
from Depto.forms import *
#form_integrantes, form_GastosFijos, form_GastosDiarios, UserRegisterForm, AvatarFormulario, UserEditForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "inicio.html", {'avatar': avatar})

def gastos(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'gastos.html', {'avatar': avatar})

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
        avatar = Avatar.objects.filter(user = request.user.id)
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

#SUPERMERCADO

def lista_super(request):
    supermercados = Supermercado.objects.all()
    if request.method == 'POST':
        supermercados = Supermercado(producto = request.POST['producto'], rubro = request.POST['rubro'], cantidad = request.POST['cantidad'])
        supermercados.save()
        supermercados = Supermercado.objects.all()
        return render(request, "supermercado.html", {"supermercados": supermercados})
    return render(request, "supermercado.html")

def update_supermercado(request, supermercado_id):
    supermercado = Supermercado.objects.get(id = supermercado_id)

    if request.method == 'POST':
        formulario = form_Supermercado(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            supermercado.producto = informacion['producto']
            supermercado.rubro = informacion['rubro']
            supermercado.cantidad = informacion['cantidad']
            supermercado.save()
            supermercados = Supermercado.objects.all() #trae todo
            return render(request, "supermercado.html", {"supermercados": supermercados})
    else:
        formulario = form_Supermercado(initial={'producto': supermercado.producto,'rubro': supermercado.rubro,'cantidad': supermercado.cantidad})
    return render(request, "update_supermercado.html", {"formulario": formulario})

def read_supermercado(request):
    supermercados = Supermercado.objects.all() #trae todo
    return render(request, "supermercado.html", {"supermercados": supermercados})

def delete_supermercado(request, supermercado_id):
    supermercado = Supermercado.objects.get(id = supermercado_id)
    supermercado.delete()
    supermercados = Supermercado.objects.all()
    return render(request, "supermercado.html", {"supermercados": supermercados}) 
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "supermercado.html", {'avatar': avatar})



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

def perfil(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'perfiles/perfil.html', {'avatar': avatar})

def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
    else:
        form = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username, 'first_name':usuario.first_name, 'last_name':usuario.last_name})
    return render(request, 'perfiles/editarPerfil.html', {'form': form, 'usuario': usuario})

def cambiarPassword(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data= request.POST, user= request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request,'cambiarPassword.html', {'form': form, 'usuario': usuario})

def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
                   
        except:
            form = AvatarFormulario()
    return render(request, 'perfiles/changeAvatar.html', {'form': form})