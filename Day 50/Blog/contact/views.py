from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    if request.method == 'POST':
        
    return render(request, 'contact.html')
