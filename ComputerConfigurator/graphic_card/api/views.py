from graphic_card.api.serializers import (Graphic_Card_IDS_Serializers,
                                          Graphic_CardSerializers)
from graphic_card.models import Grafic_Card
from cpu.api.permissions import IsAdminCreatorOrReadOnly

from rest_framework import viewsets


class AllGraphic_CardsViewSet(viewsets.ModelViewSet):
    serializer_class = Graphic_CardSerializers
    permission_classes = [IsAdminCreatorOrReadOnly]

    def get_queryset(self):
        return Grafic_Card.objects.all().order_by("-id")
        # return self.request.user.accounts.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AllGraphic_Card_IDSViewSet(viewsets.ModelViewSet):
    serializer_class = Graphic_Card_IDS_Serializers
    permission_classes = [IsAdminCreatorOrReadOnly]

    def get_queryset(self):
        return Grafic_Card.objects.all().order_by("-id")
        # return self.request.user.accounts.all()
