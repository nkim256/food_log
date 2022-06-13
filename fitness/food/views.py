from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from food.models import Food, Entry
from food.serializers import (
    FoodSerializer,
    # RecipeSerializer,
    EntrySerializer,
)
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'food': reverse('food-list', request=request, format=format),
        # 'recipe': reverse('recipe-list', request=request, format=format),
        'entry': reverse('entry-list', request=request, format=format),
    })
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    #might need to set lookup_field
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

# class ComponentList(generics.ListCreateAPIView):
#     queryset = Component.objects.all()
#     serializer_class = ComponentSerializer


# class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
#     #might need to set lookup_field
#     queryset = Component.objects.all()
#     serializer_class = ComponentSerializer

# class RecipeList(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer


# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     #might need to set lookup_field
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer