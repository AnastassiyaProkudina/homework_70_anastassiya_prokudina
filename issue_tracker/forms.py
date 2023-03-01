from django import forms
from django.core.exceptions import ValidationError

from issue_tracker.models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        type_old = forms.ModelChoiceField(queryset=Type.objects.all())
        status = forms.ModelChoiceField(queryset=Status.objects.all())
        fields = ["summary", "status", "type_old", "description"]

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if len(summary) < 2:
            raise ValidationError("Заголовок должен быть длиннее двух символов")
        return summary
