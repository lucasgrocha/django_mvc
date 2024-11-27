from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_list_json(request):
    tasks = Task.objects.all()
    data = {
        'tasks': [
            {
                'id': task.id,
                'name': task.name,
                'completed': task.completed,
            } for task in tasks
        ]
    }
    return JsonResponse(data)
