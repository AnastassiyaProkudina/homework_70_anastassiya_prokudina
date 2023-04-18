from django.db import models
from django.utils import timezone


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок",
        default="No summary",
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Описание",
    )
    status = models.ForeignKey(
        to="issue_tracker.Status",
        related_name="Статус",
        blank=True,
        on_delete=models.PROTECT,
    )
    type = models.ManyToManyField(
        to="issue_tracker.Type",
        related_name="issues",
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False,
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None,
    )
    project = models.ForeignKey(
        to="issue_tracker.Project",
        related_name="issues",
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"id: {self.id}; summary: {self.summary};"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
