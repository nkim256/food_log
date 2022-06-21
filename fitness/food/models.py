from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from datetime import date
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Food(models.Model):
    name = models.CharField(max_length = 100, unique = True, default = "")
    calories = models.FloatField(default = 0)
    protein = models.FloatField(default = 0)
    carbs = models.FloatField(default = 0)
    fat = models.FloatField(default = 0)
    def __str__(self):
        return self.name
    
class Entry(models.Model):
    component = models.ForeignKey(Food, blank = True, null = True, on_delete= models.DO_NOTHING)
    date = models.DateField()
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
    calorie_goal = models.FloatField(default = 0)
    protein_goal = models.FloatField(default = 0)
    carbs_goal = models.FloatField(default = 0)
    fat_goal = models.FloatField(default = 0)
    curr_calories = models.FloatField(default = 0)
    curr_protein = models.FloatField(default = 0)
    curr_carbs = models.FloatField(default = 0)
    curr_fat = models.FloatField(default = 0)
    weight = models.FloatField(default = 0)
    date = models.DateField()


