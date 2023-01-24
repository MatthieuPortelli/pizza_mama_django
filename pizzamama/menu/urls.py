from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),    # Pour déterminer la vue du chemin url 'menu', dans le fichier views.py
]
