# In vs code ctrl+shift+p > python:select interpreter >select env(for import error)
# Ref: https://www.bezkoder.com/django-rest-api/

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializer import TodoSerializer
from .models import Todo
import uuid
import logging

def home(request):
    return render(request,"index.html")

@api_view(['Get'])
def index(request):
    try:
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=422)


@api_view(['POST'])
def store(request):
    try:
        updatedData = request.data #req.data gives parsed data
        generated_id = f"{uuid.uuid4()}"
        updatedData["id"] = generated_id  
        serializer = TodoSerializer(data = updatedData) # seriliazes data to model 
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)},status=500)


@api_view(['GET'])
def show(request, todoId):
    try:
        todo = Todo.objects.get(id = todoId)
        serializer = TodoSerializer(todo, many= False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": "Todo not found"}, status=404)


@api_view(['PATCH'])
def update(request, todoId):
    try:
        todo = Todo.objects.get(id = todoId)
        serializer = TodoSerializer(todo, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": "Todo not found"}, status=404)


@api_view(['DELETE'])
def delete(request, todoId):
    try:
        todo = Todo.objects.get(id = todoId)
        todo.delete()
        return Response({"message": "Item Successfully Deleted"})
    except Exception as e:
        return Response({"message": "Todo not found"}, status=404)