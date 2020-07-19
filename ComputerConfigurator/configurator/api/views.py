from rest_framework import viewsets
from configurator.models import Configurator
from configurator.api.serializers import (All_Configurator_Serializer,
                                          All_Configurator_IDs_Serializer)


class All_Configurator_Viewset(viewsets.ModelViewSet):
    serializer_class = All_Configurator_Serializer

    def get_queryset(self):
        return Configurator.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_Configurator_IDs_Viewset(viewsets.ModelViewSet):

    serializer_class = All_Configurator_IDs_Serializer

    def get_queryset(self):
        return Configurator.objects.all().order_by("-id")
