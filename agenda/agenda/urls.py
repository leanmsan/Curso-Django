from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contacto', include('Contacto.urls')),
    path('Tarea/', include('Tarea.urls')),
    path('', views.index, name='index')
]
