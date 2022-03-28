from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Footer, Testimonial, Telephone

def index(request):
    mero_footer = Footer.objects.all
    mero_testimonials = Testimonial.objects.all
    mero_number = Telephone.objects.all

    return render(request, 'index.html', {'footer': mero_footer, 'testimonials': mero_testimonials, 'number': mero_number})