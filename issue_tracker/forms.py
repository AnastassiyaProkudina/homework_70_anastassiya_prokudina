from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple

from issue_tracker.models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=CheckboxSelectMultiple)

    class Meta:
        model = Issue

        status = forms.ModelChoiceField(queryset=Status.objects.all())
        fields = ["summary", "type", "status", "description"]

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if len(summary) < 2:
            raise ValidationError("Заголовок должен быть длиннее двух символов")
        return summary
