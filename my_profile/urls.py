from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.my_profile, name='about-me'),
]
