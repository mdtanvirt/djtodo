from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ToDoSerializer
from .models import Todo

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serilizer_class = ToDoSerializer
    queryset = Todo.objects.all()
