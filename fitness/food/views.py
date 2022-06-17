from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from food.models import *
from food.serializers import *
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
        'instance': reverse('instance-list', request=request, format=format),
    })



class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    #might need to set lookup_field
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class InstanceList(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
