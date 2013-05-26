from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')
def login(request):
    return render_to_response('login.html')
def nosotros(request):
    return render_to_response('nosotros.html')
def horario(request):
    return render_to_response('horario.html')
def reservar(request):
    return render_to_response('reservar.html')
