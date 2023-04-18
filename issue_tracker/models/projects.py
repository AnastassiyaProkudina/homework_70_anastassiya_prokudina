from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    started_at = models.DateField(verbose_name="Дата начала")
    finished_at = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    title = models.CharField(
        max_length=200, verbose_name="Название", blank=False, null=False
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Описание",
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
    users = models.ManyToManyField(
        through="issue_tracker.UserProjects", to=User, related_name="users_projects"
    )

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
