from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.user_login, name='login'),
    path('register/', views.registro_view, name='register'),
]


