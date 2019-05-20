# Register your models here.

from django import forms
from django.contrib import admin

from .models import Projects


class ProjectsAdminForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsAdmin(admin.ModelAdmin):
    form = ProjectsAdminForm
    list_display = ['project_name', 'github_link', 'youtube_link', 'points_awarded', 'user_id',
                    'assessor_id']
    readonly_fields = ['project_name', 'github_link', 'youtube_link', 'points_awarded',
                       'user_id', 'assessor_id']


admin.site.register(Projects, ProjectsAdmin)
