from django import forms
from django.forms import ModelForm
from .models import Recipes


class NewRecipe(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
    # recipe = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Enter recipe name"}),
    # ),

    # calories = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"class": "form-control",
    #                "placeholder": "enter amount of calories"}
    #     )
    # ),

    # duration = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"class": "form-control",
    #                "placeholder": "enter the duration"}
    #     )
    # )
