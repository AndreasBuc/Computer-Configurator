from software.models import (Games, OfficeWare, Operating_System)
from software.api.serializers import (All_Games_Serializer,
                                      All_Games_IDs_Serializer,
                                      All_OfficeWare_Serializer,
                                      All_OfficeWare_IDs_Serializer,
                                      All_Operating_System_Serializer,
                                      All_Operating_System_IDs_Serializer)

from rest_framework import viewsets


class All_Games_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_Games_Serializer

    def get_queryset(self):
        return Games.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_Games_IDs_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_Games_IDs_Serializer

    def get_queryset(self):
        return Games.objects.all().order_by("-id")


class All_OfficeWare_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_OfficeWare_Serializer

    def get_queryset(self):
        return OfficeWare.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_OfficeWare_IDs_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_OfficeWare_IDs_Serializer

    def get_queryset(self):
        return OfficeWare.objects.all().order_by("-id")


class All_Operating_System_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_Operating_System_Serializer

    def get_queryset(self):
        return Operating_System.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_Operating_System_IDs_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_Operating_System_IDs_Serializer

    def get_queryset(self):
        return Operating_System.objects.all().order_by("-id")
