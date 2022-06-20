from django.forms import ModelForm
from django import forms
from .models import *

class CreateFood(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'protein', 'carbs', 'fat']
class CreateEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['food','date', 'serving']
class CreateInstance(forms.ModelForm):
    class Meta:
        model = Instance
        fields = [
            'calorie_goal',
            'protein_goal', 
            'carbs_goal',
            'fat_goal',
            'curr_calories',
            'curr_protein',
            'curr_carbs',
            'curr_fat',
            'weight',
            'date'
            ]