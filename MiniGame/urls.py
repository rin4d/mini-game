from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Django
    path('', include('games.urls')),  # Inclure les URLs de l'application "games"
]
