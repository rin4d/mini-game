from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pour la page d'accueil
    path('', views.login_view, name='login'),  # Route pour la connexion
]
