from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Food(models.model):
    serving_size = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
class Component(models.model):
    #Either have a food 
    food = models.ForeignKey(Food, on_delete = models.DO_NOTHING)
    serving_size = models.FloatField()
class Recipe(models.model):
    components = models.ForeignKey(Component, on_delete= models.DO_NOTHING)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()   

class Entry(models.model):
    component = models.ForeignKey(Recipe, blank = True, null = True)
    date = models.CharField()



