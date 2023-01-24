from django.shortcuts import render     # Permet d'aller chercher un template
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.
def index(request):
    # pizzas = Pizza.objects.all()                                                                    # Je récupère l'objet Pizza de la bdd avec ses informations
    # pizzas_names_and_prices = [pizza.name + " : " + str(pizza.price) + "€" for pizza in pizzas]     # Je stocke les noms et prix des pizzas dans une liste
    # pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)                                # Je transforme en chaine de caractères
    # return HttpResponse("Les pizzas : " + pizzas_names_and_prices_str)                              # Ce qui sera affiché à l'écran au chemin url 'menu'

    pizzas = Pizza.objects.all().order_by('price')                  # Je passe tout l'objet Pizza
    return render(request, 'menu/index.html', {'pizzas': pizzas})   # Appel de mon rendu index.html, définition de la clé 'pizzas' pour passer les données au rendu

def api_get_pizzas(request):
    pizzas = Pizza.objects.all()                                    # Dans 'pizzas' j'ai une liste d'objets de type Pizza
    json = serializers.serialize("json", pizzas)                    # Je serialize au format json 'pizzas'
    return HttpResponse(json)
