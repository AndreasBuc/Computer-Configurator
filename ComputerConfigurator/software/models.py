from django.db import models
from django.conf import settings


class Games(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='games')

    def __str__(self):
        return self.name


class OfficeWare(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='officewares')

    def __str__(self):
        return self.name


class Operating_System(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='os')

    def __str__(self):
        return self.name
