"""SCCC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.views import login,logout_then_login
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('apps.cultivo.urls',namespace="cultivo_vacio")),
    url(r'^cultivo/',include('apps.cultivo.urls',namespace="cultivo")),
    url(r'^cultivo/',include('apps.cosecha.urls',namespace="cosecha")),
    url(r'^cultivo/',include('apps.usuario.urls',namespace="usuario")),
    url(r'^accounts/login/', login, {'template_name':'Login/index.html'}, name='login' ),
    url(r'^logout/',logout_then_login, name='logout'),
]
