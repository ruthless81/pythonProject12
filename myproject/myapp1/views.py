from django.shortcuts import render
from django.http import JsonResponse
from .models import Car, Animal
from .serializers import CarSerializer, AnimalSerializer
from rest_framework import generics




def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    data = {
        'make': car.make,
        'model': car.model,
        'year': car.year,
    }
    return JsonResponse(data)

def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    data = {
        'name': animal.name,
        'species': animal.species,
        'age': animal.age,
    }
    return JsonResponse(data)

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer










