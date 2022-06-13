from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from datetime import date
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Food(models.Model):
    name = models.CharField(max_length = 100, unique = True, default = "")
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    def __str__(self):
        return self.name
    

# class Recipe(models.Model):
#     name = models.CharField(max_length=100, default = '')
#     components = models.ForeignKey(Component, on_delete= models.DO_NOTHING)
#     calories = models.FloatField()  
#     protein = models.FloatField()
#     carbs = models.FloatField()
#     fat = models.FloatField()   

class Entry(models.Model):
    food = models.ForeignKey(Food, blank = True, null = True, on_delete= models.DO_NOTHING)
    date = date.today()
    serving = models.FloatField()




