from food.models import(
    Food,
    # Recipe,
    Entry
)
from rest_framework import serializers

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = [ 'name', 'calories', 'protein', 'carbs', 'fat']


# class RecipeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ['name', 'components', 'calories', 'protein', 'carbs', 'fat']
class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['food', 'date', 'serving']


