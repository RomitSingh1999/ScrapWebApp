from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('getdata',views.scrap, name='getdata'),
    path ('logout',views.logout, name='logout'),
    path('amazon',views.amazon, name='amazon'),
    
]