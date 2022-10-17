from django.urls import path
from Depto.views import *
from django.contrib.auth.views import LogoutView

from Depto.views import *

urlpatterns = [
    path('inicio/', inicio),
    #integrantes
    path('integrantes/', integrantes),
    path('buscar_integrantes/', buscar_integrantes),
    path('create_integrantes/', create_integrantes),
    path('read_integrantes/', read_integrantes),
    path('update_integrantes/<integrante_id>', update_integrantes),
    path('delete_integrantes/<integrante_id>', delete_integrantes),
    #gastos general
    path('gastos/', gastos),
    #gastos fijos
    path('gastosFijos/', gastosFijos),
    path('create_gastosF/', create_fijos),
    path('read_gastosF/', read_fijos),
    path('update_gastosF/<gastoF_id>', update_fijos),
    path('delete_gastosF/<gastoF_id>', delete_fijos),
    path('buscar_fijos/', buscar_fijos),
    #gastos diarios
    path('gastosDiarios/', gastosDiarios),
    path('create_gastosD/', create_diarios),
    path('read_gastosD/', read_diarios),
    path('update_gastosD/<gastoD_id>', update_diarios),
    path('delete_gastosD/<gastoD_id>', delete_diarios),
    path('buscar_diarios/', buscar_diarios),
    #tareas
    path('supermercado/', lista_super),
    #logout
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name = "Logout"),
    #login
    path('login/', login_request),
    #registro
    path('registro/', registro),
    #perfil
    path('perfil/', perfil),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/cambiarPassword/', cambiarPassword),
    path('perfil/changeAvatar/', AgregarAvatar),
]

