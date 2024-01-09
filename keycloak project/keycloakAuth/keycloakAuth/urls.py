"""
URL configuration for keycloakAuth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from myApi.views import keycloak_login
from django.shortcuts import render

from myApi.auth_utils import api_view_wrapper
# from myApi.views import keycloak_login
# from django.contrib.auth.decorators import login_required
# from . import views




urlpatterns = [
    path('api/', include('myApi.urls')),
    path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),

    # path('accounts/', include('allauth.urls')),
    # path('keycloak-login/', keycloak_login, name='keycloak-login'),
]
