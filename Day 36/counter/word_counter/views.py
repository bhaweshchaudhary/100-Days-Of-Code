from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def counter(request):
    text = request.GET['text']
    text_count = text.split()
    text_counted = len(text_count)
    return render(request, 'counter.html', {text_counted: 'text'})