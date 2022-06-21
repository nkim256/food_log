from food.models import (
    Food, 
    Entry,
    CalorieGoal,
    ProteinGoal,
    CarbGoal,
    FatGoal,
    Instance
)
from rest_framework import serializers

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = [ 'name', 'calories', 'protein', 'carbs', 'fat']

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['component', 'date', 'serving']

class CalorieGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CalorieGoal
        fields = ['count']

class ProteinGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProteinGoal
        fields = ['count']

class CarbGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarbGoal
        fields = ['count']

class FatGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FatGoal
        fields = ['count']

class InstanceSerializer(serializers.HyperlinkedModelSerializer):
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
            'date',
            ]





