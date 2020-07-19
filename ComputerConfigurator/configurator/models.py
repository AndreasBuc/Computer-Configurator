from django.db import models
from django.conf import settings
from cpu.models import CPU
from graphic_card.models import Grafic_Card
from software.models import Games, OfficeWare, Operating_System


class Configurator(models.Model):
    name = models.CharField(max_length=256, unique=True)
    cpu = models.ForeignKey(to=CPU,
                            on_delete=models.SET_NULL,
                            related_name='configurations',
                            blank=True,
                            null=True)
    grafic_card = models.ForeignKey(to=Grafic_Card,
                                    on_delete=models.SET_NULL,
                                    related_name='configurations',
                                    blank=True,
                                    null=True)
    operating_system = models.ForeignKey(to=Operating_System,
                                         on_delete=models.SET_NULL,
                                         related_name='configurations',
                                         blank=True,
                                         null=True)
    games = models.ManyToManyField(to=Games,
                                   related_name='configurations',
                                   blank=True)

    officewares = models.ManyToManyField(to=OfficeWare,
                                         related_name='configurations',
                                         blank=True)

    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='configurations')

    def __str__(self):
        return self.name
