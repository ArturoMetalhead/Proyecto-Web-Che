from django.urls import path
from WebCheApp import views

urlpatterns = [
    path('', views.home, name='home'),
]
