from django.contrib.auth.models import User
from django.db import models

from issue_tracker.models import Project


class UserProjects(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='user_projects',
        verbose_name='Проекты пользователя',
        null=False,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name='user_projects',
        verbose_name='Проекты пользователя',
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Проект пользователя'
        verbose_name_plural = 'Проекты пользователя'

    def __str__(self):
        return f"project: {self.project_id}; user: {self.user_id};"
