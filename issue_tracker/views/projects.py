from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

from issue_tracker.forms import SimpleSearchForm, ProjectForm, UserProjectsForm
from issue_tracker.models import Project, Issue, UserProjects


class ProjectListView(ListView):
    template_name = "projects/project_list.html"
    model = Project
    context_object_name = "projects"
    ordering = ("-id",)

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(
                description__icontains=self.search_value
            )
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
        return context


class ProjectDetail(DetailView):
    template_name = "projects/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = Issue.objects.filter(project_id=self.object.pk)
        context["issues"] = issues
        return context


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "projects/project_update.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse("issue_tracker:project_detail", kwargs={"pk": self.object.pk})


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/project_create.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("issue_tracker:project_detail", kwargs={"pk": self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "projects/project_confirm_delete.html"
    model = Project
    success_url = reverse_lazy("issue_tracker:index")


class ProjectUserAddView(LoginRequiredMixin, CreateView):
    model = UserProjects
    form_class = UserProjectsForm
    template_name = "projects/project_add_user.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        object = form.save(commit=False)
        object.project = project
        object.save()
        form.save_m2m()
        return redirect("issue_tracker:project_detail", pk=project.pk)


class ProjectUserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "projects/project_delete_user.html"
    model = Project
    form_class = UserProjectsForm
    confirm_delete = False

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.object.pk)
        obj = form.save(commit=False)
        project.users.remove(obj.user)
        return redirect("issue_tracker:project_detail", pk=self.object.pk)
