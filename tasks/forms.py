from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "start_date": forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            "due_date": forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            "project": forms.Select(attrs={'class': 'form-control'}),
            "assignee": forms.Select(attrs={'class': 'form-control'}),
        }
