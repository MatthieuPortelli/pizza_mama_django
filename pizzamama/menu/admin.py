from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'vegetarian', 'price')   # Pour afficher tous les détails dans la partie admin
    search_fields = ['name']                                        # Pour rajouter un champ de recherche dans la partie admin


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
