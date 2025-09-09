from django.http import HttpResponse
from django.shortcuts import redirect

def app2_home(request):
    return HttpResponse('<h1>Bem-vindo ao App2!</h1><a href="/primeiro/">Ir para Primeiro App</a>')

def go_primeiro(request):
    return redirect('/primeiro/')
