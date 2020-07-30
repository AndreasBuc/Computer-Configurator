from django.db import models
from django.conf import settings


class CPU(models.Model):
    manufacturer = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    kernel = models.PositiveIntegerField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)

    price = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='cpus')

    def __str__(self):
        return f'{self.manufacturer} {self.model}, {self.kernel}x {self.speed} GHz'
