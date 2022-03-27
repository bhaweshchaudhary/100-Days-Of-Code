from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Footer

def index(request):
    mero_footer = Footer.objects.all
    return render(request, 'index.html', {'footer':mero_footer})