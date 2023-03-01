from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Тип",
        null=False,
        blank=False,
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
