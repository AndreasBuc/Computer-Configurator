from rest_framework import viewsets
from cpu.api.serializers import CPUSerializer, CPU_IDs_Serializer
from cpu.api.permissions import IsAdminCreatorOrReadOnly
from cpu.models import CPU


class AllCPUSViewSet(viewsets.ModelViewSet):
    serializer_class = CPUSerializer
    permission_classes = [IsAdminCreatorOrReadOnly]

    def get_queryset(self):
        return CPU.objects.all().order_by("-id")
        # return self.request.user.accounts.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AllCPUSIDSViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = CPU_IDs_Serializer

    def get_queryset(self):
        return CPU.objects.all().order_by("-id")
