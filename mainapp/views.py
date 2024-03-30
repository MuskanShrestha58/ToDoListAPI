from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Read


class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Update


class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Create


class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Delete


class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
