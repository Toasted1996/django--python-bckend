"""
URL configuration for giorthyLopezProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from giorthyApp.views import inicio, bici_montana, bici_electrica, bici_bmx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('bicicleta/montana/', bici_montana, name='bici_montana'),
    path('bicicleta/electrica/', bici_electrica, name='bici_electrica'),
    path('bicicleta/bmx/', bici_bmx, name='bici_bmx'),
]
