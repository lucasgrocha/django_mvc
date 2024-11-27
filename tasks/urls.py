from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('api/tasks/', views.task_list_json, name='task_list_json'),
]
