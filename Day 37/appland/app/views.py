from email import message
from email.header import Header
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                messages.info(request, 'accounts successfully created')
                user.save()
                return redirect('register')
        else:
            messages.info(request, 'Password not matched')
            return redirect('register')
    else:
        return render(request, 'register.html')
    