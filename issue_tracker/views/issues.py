from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from issue_tracker.forms import IssueForm, ProjectIssueForm
from issue_tracker.models import Issue, Project


class IssueDetail(DetailView):
    template_name = "issues/issue.html"
    model = Issue


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "issues/issue_update.html"
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse("issue_detail", kwargs={"pk": self.object.pk})


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/issue_create.html"
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse("issue_detail", kwargs={"pk": self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "issues/issue_confirm_delete.html"
    model = Issue
    success_url = reverse_lazy("index")


class IssueConfirmDeleteView(LoginRequiredMixin, TemplateView):
    template_name = "issues/issue_confirm_delete.html"

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=kwargs["pk"])
        context["issue"].delete()
        return redirect("index")


class ProjectIssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = ProjectIssueForm
    template_name = "issues/project_issue_create.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        print(f"project {project}")
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect("project_detail", pk=project.pk)
