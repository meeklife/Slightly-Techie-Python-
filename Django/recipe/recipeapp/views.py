from django.shortcuts import render
from .models import Recipes

from django.http import HttpResponseRedirect
from .forms import NewRecipe

# Create your views here.


def home(request):
    all_recipes = Recipes.objects.all()
    data = {'recipes': all_recipes}
    # print(data)
    return render(request, 'home.html', data)


def create_recipes(request):
    return render(request, 'new.html')


def update_recipe_page(request, recipe_id):
    recipe = Recipes.objects.filter(id=recipe_id)
    return render(request, 'edit.html', {'recipes': recipe})
