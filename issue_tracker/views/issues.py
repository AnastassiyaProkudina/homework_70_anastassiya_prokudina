from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from issue_tracker.forms import IssueForm
from issue_tracker.models import Issue


class IssueDetail(TemplateView):
    template_name = "issues/issue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=kwargs["pk"])
        return context


class IssueUpdateView(FormView):
    template_name = "issues/issue_update.html"
    form_class = IssueForm

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.issue.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)


class IssueCreateView(FormView):
    template_name = "issues/issue_create.html"
    form_class = IssueForm

    def form_valid(self, form):
        issue = form.save()
        return redirect("issue_detail", pk=issue.pk)


class IssueDeleteView(TemplateView):
    template_name = "issues/issue_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=kwargs["pk"])
        return context


class IssueConfirmDeleteView(TemplateView):
    template_name = "issues/issue_confirm_delete.html"

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=kwargs["pk"])
        context["issue"].delete()
        return redirect("index")
