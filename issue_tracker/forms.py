from django import forms
from django.core.validators import BaseValidator

from issue_tracker.models import Issue, Type, Status, Project


class CustomMaxLenValidator(BaseValidator):
    def __init__(self, limit_value=30):
        self.limit_value = limit_value
        message = "Максимальная длина заголовка задачи %(limit_value)s. Вы ввели %(show_value)s символов."
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)


class CustomMinLenValidator(BaseValidator):
    def __init__(self, limit_value=2):
        self.limit_value = limit_value
        message = "Минимальная длина заголовка %(limit_value)s символов. Вы ввели %(show_value)s символов"
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value < limit_value

    def clean(self, value):
        return len(value)


class IssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label="Тип",
    )
    summary = forms.CharField(
        validators=(CustomMaxLenValidator(), CustomMinLenValidator()), label="Заголовок"
    )

    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")

    class Meta:
        model = Issue
        fields = ["summary", "type", "status", "project", "description"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "started_at", "finished_at", "description"]
        widgets = {
            "started_at": forms.DateInput(attrs={"type": "date"}),
            "finished_at": forms.DateInput(attrs={"type": "date"}),
        }


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Поиск")


class ProjectIssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label="Тип",
    )
    summary = forms.CharField(
        validators=(CustomMaxLenValidator(), CustomMinLenValidator()), label="Заголовок"
    )

    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статус")

    class Meta:
        model = Issue
        fields = ["summary", "type", "status", "description"]
