from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, 'main_page.html')  
urlpatterns = [
    path('simple-api/', login_required(views.simple_api_view), name='simple_api_view'),
    path('main/', login_required(main_page)),
]