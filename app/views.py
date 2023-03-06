from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def skypiea(request):
    return HttpResponse('<marquee><h1>luffy is sun god nika </h1></marquee>')
