from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_recipes, name='create_recipes'),
    path('create/', api_views.create_new_recipes, name='create_new_recipes'),
    path("show/<int:recipe_id>", api_views.view_recipe, name='view_recipe'),
    path("edit/<int:recipe_id>", views.update_recipe_page, name='edit_recipe'),
    path("update/<int:recipe_id>",
         api_views.update_recipe, name='update_recipe'),
    path("delete/<int:recipe_id>",
         api_views.delete_recipe, name='delete_recipe'),


]
