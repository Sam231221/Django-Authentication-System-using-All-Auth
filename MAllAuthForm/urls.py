from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
   path('accounts/', include('allauth.urls')),
   path('',HomeView, name="home")
]
