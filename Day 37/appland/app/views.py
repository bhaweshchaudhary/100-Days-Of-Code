from email.header import Header
from django.shortcuts import render, HttpResponse
from .models import Header, SecondSection

# Create your views here.
def app(request):
    my_header = Header()
    second = SecondSection()
    my_header.head = "App Land"
    my_header.main_text = "Promote Your App with App Land"
    my_header.desc = "We can promote your App better than anyone."
    second.head = "Save your time using App Land"
    return render(request, 'index.html', {"logo": my_header.head, "main_text": my_header.main_text, "desc": my_header.desc, "second_head": second.head})
