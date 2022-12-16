from django.forms import ModelForm
from projects.models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "owner": forms.Select(attrs={'class': 'form-control'}),
        }
