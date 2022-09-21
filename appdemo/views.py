from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hi, I am a index page")

def hello(request):
    return HttpResponse("hi, I am a hello pag")
