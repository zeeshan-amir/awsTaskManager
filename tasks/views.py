from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer


@api_view(['POST'])
def create_task(request):
    task = Task.create_task(
        title=request.data['title'],
        description=request.data['description']
    )
    return Response(task, status=201)


@api_view(['GET'])
def list_tasks(request):
    tasks = Task.list_tasks()
    return Response(tasks)


@api_view(['GET'])
def get_task(request, task_id):
    task = Task.get_task(task_id)
    if task:
        return Response(task)
    return Response({"error": "Task not found"}, status=404)


@api_view(['PUT'])
def update_task(request, task_id):
    task = Task.update_task(
        task_id=task_id,
        title=request.data['title'],
        description=request.data['description']
    )
    return Response(task)


@api_view(['POST'])
def complete_task(request, task_id):
    task = Task.complete_task(task_id)
    return Response(task)
