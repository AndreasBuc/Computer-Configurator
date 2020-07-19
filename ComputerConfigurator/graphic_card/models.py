from django.db import models
from django.conf import settings


class Grafic_Card(models.Model):
    manufacturer = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    memory_size = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='graphic_cards')

    def __str__(self):
        return f'{self.manufacturer} {self.model}, {self.memory_size}'
