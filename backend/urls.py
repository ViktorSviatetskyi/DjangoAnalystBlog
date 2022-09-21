from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='backend-home'),
    path('about/', views.about, name='backend-about'),
]
