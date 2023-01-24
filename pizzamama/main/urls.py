from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),    # Pour déterminer la vue du chemin url 'menu', dans le fichier views.py
]