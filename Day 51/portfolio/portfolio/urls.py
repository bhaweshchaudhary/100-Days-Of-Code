from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
]
