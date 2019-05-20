from django import forms

from .models import Projects


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'github_link', 'user_id', 'assessor_id']
