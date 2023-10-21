from django.db import models

# Create your models here.


class Recipes(models.Model):
    name = models.CharField(max_length=200)
    calories = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name},  {self.calories} calories,  {self.duration}"
