from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<title>ShanthiMadugundi website</title><h2><center>THIS IS SHANTHIMADUGUNDI PAGE</CENTER></H2>")