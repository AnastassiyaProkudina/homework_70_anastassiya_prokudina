from django.db import models


class Project(models.Model):
    started_at = models.DateField(
        verbose_name="Дата начала"
    )
    finished_at = models.DateField(
        verbose_name="Дата окончания",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
        blank=False,
        null=False
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    def __str__(self):
        return f'title: {self.title};'
