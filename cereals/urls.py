from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    
    
    path('',views.login,name="login"),
    path('home',views.main,name='main'),
    path('change',views.change,name='change'),
    path('logout',views.logout,name='logout'),

]