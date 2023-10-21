from django.shortcuts import render
from .models import Recipes
from rest_framework.response import Response
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view


@api_view(["POST"])
def create_new_recipes(request):
    if request.method == "POST":
        data = request.data
    # create recipe in db
        serializer = RecipeSerializer(data=data)
    # validate user data
        if serializer.is_valid():
            serializer.save()
            all_recipes = Recipes.objects.all()
            data = {'recipes': all_recipes}
            return render(request, 'home.html', data)
        else:
            return Response(serializer.errors, status=400)


@api_view(["GET"])
def view_recipe(request, recipe_id):
    recipe = Recipes.objects.filter(id=recipe_id)
    if recipe:
        serializer = RecipeSerializer(recipe)
        data = {'recipes': recipe}
        return render(request, 'show.html', data)


@api_view(["PATCH"])
def update_recipe(request, recipe_id):
    recipe = Recipes.objects.filter(id=recipe_id)
    if recipe:
        data = request.data
        serializer = RecipeSerializer(recipe, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'recipes': recipe}
            return render(request, 'show.html', data)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response('Recipes not found', status=404)


@api_view(['DELETE'])
def delete_recipe(request, recipe_id):
    recipe = Recipes.objects.filter(id=recipe_id)
    if recipe:
        recipe.delete()
        all_recipes = Recipes.objects.all()
        data = {'recipes': all_recipes}
        return render(request, 'home.html', data)
