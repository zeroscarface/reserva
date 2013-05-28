from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import Template, RequestContext

from models import *
import datetime

def index(request):
    noticias = Noticia.objects.filter()
    state = rol = ''
    state = check(request)
    if state == 'in':	
        if not request.user.is_superuser:
            rol = 'usuario'
        else:
            rol = 'administrador'
    return render_to_response('index.html',{'noticias': noticias,'rol':rol,'state':state},context_instance=RequestContext(request))

def logout_user(request):
    state = check(request)
    if state == 'in':	
	username = request.user.username
        logout(request)
        state = 'out'
	mensaje =  username + ' cerro sesion exitosamente'
    else: 
        mensaje = 'Warning'
    return render_to_response('login.html',{'state':state,'mensaje':mensaje},context_instance=RequestContext(request))
    

def check(request):
    if request.user.is_authenticated():
        return 'in'
    else:
        return 'out'


def login_user(request):
    state = check(request)
    username = password = mensaje = ''
    if state == 'in':
        mensaje = "Usuario: " + request.user.username
    if request.POST:
        if state == 'in':
            username = request.user.username
            mensaje = "Usuario: " + username
        else:    
            mensaje = "Por favor introduce tus datos..."
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    mensaje = username + " inicio sesion exitosamente"
                    state= 'in'
                else:
                    mensaje = 'Su cuenta ha sido desabilitada. Comuniquese con un miembro del LDAC'
                    state = 'out'
            else:
                state = 'out'
                mensaje = "Su contrasena y/o usuario son incorrectos. Intente de nuevo."
    return render_to_response('login.html',{'state':state, 'username': username, 'mensaje': mensaje},context_instance=RequestContext(request))

def nueva_noticia(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        Noticia.objects.create(titulo=titulo,contenido=contenido)
    return index(request)

def eliminar_noticia(request):
    noticia= request.POST.get('titulo')
    Noticia.objects.filter(titulo=noticia).delete()
    return index(request)

def limpiar_noticias(request):
    for n in Noticia.objects.filter():
        n.delete()
    return index(request)
    

def nosotros(request):
    state = check(request)
    return render_to_response('nosotros.html',{'state': state})

def horario(request):
    state = check(request)
    return render_to_response('horario.html',{'state': state})
def reservar(request):
    state = check(request)
    return render_to_response('reservar.html',{'state': state})
