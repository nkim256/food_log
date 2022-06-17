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
    
class Entry(models.Model):
    food = models.ForeignKey(Food, blank = True, null = True, on_delete= models.DO_NOTHING)
    date = date.today()
    serving = models.FloatField()

class CalorieGoal(models.Model):
    count = models.FloatField()

class ProteinGoal(models.Model):
    count = models.FloatField()

class CarbGoal(models.Model):
    count = models.FloatField()

class FatGoal(models.Model):
    count = models.FloatField()

class Instance(models.Model):
    calorie_goal = models.FloatField()
    protein_goal = models.FloatField()
    carbs_goal = models.FloatField()
    fat_goal = models.FloatField()
    curr_calories = models.FloatField()
    curr_protein = models.FloatField()
    curr_carbs = models.FloatField()
    curr_fat = models.FloatField()
    weight = models.FloatField()
    date = date.today()




