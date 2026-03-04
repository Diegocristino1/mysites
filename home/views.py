from django.shortcuts import render
from django.http import HttpResponse

# criando o hello word

def hello_world(request):
    return HttpResponse("Hello World!")
