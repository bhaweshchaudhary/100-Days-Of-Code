from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("you're in the home page, goto polls.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('polls/', include('polls.urls')),
]
