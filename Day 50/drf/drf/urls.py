from django.contrib import admin
from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test')
]
