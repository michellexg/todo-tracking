from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = TaskForm()

    context = {"form": form}

    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"tasks": tasks}

    return render(request, "tasks/show_my_tasks.html", context)


@login_required
def search_tasks(request):
    searched = request.POST['searched']
    tasks = Task.objects.filter(name__contains=searched)
    context = {
        "searched": searched,
        "tasks": tasks,
    }
    return render(request, "tasks/search_tasks.html", context)
