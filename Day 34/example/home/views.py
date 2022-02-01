from django.shortcuts import render, HttpResponse
from .models import Book


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dynamic(request, name):
    return HttpResponse(f'Hello your string is {name}')
