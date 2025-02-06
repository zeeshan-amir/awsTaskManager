from django.urls import path
from .views import create_task, list_tasks, get_task, update_task, complete_task

urlpatterns = [
    path('tasks/', list_tasks, name="list_tasks"),
    path('tasks/create/', create_task, name="create_task"),
    path('tasks/<str:task_id>/', get_task, name="get_task"),
    path('tasks/<str:task_id>/update/', update_task, name="update_task"),
    path('tasks/<str:task_id>/complete/', complete_task, name="complete_task"),
]
