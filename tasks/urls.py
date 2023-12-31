from django.urls import path
from .views import create_task, show_my_tasks, search_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("search/", search_tasks, name="search_tasks"),
]
