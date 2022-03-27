from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Footer, Testimonial

def index(request):
    mero_footer = Footer.objects.all
    mero_testimonials = Testimonial.objects.all
    return render(request, 'index.html', {'footer': mero_footer, 'testimonials': mero_testimonials})