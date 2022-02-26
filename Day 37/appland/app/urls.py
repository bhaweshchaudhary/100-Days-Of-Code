from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('register', views.register, name='register')
]
