from django.shortcuts import render_to_response
from models import *
import datetime

def index(request):
    noticias = Noticia.objects.filter()
    return render_to_response('index.html',{'noticias': noticias})

def login(request):
    return render_to_response('login.html')
def nosotros(request):
    return render_to_response('nosotros.html')
def horario(request):
    return render_to_response('horario.html')
def reservar(request):
    return render_to_response('reservar.html')
