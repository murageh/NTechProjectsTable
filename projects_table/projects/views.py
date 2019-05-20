# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .forms import ProjectsForm
from .models import Projects


class ProjectsListView(ListView):
    model = Projects

    class ProjectsCreateView(CreateView):
        model = Projects
        form_class = ProjectsForm

    class ProjectsDetailView(DetailView):
        model = Projects

    class ProjectsUpdateView(UpdateView):
        model = Projects
        form_class = ProjectsForm
