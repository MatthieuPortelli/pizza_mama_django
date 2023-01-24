from django.shortcuts import render     # Permet d'aller chercher un template


def index(request):
    return render(request, 'main/index.html')
