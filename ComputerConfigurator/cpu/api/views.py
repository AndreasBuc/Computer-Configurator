from rest_framework import status, viewsets
from cpu.api.serializers import CPUSerializer, CPU_IDs_Serializer

from cpu.models import CPU


class AllCPUSViewSet(viewsets.ModelViewSet):
    serializer_class = CPUSerializer

    def get_queryset(self):
        return CPU.objects.all().order_by("-id")
        # return self.request.user.accounts.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AllCPUSIDSViewSet(viewsets.ModelViewSet):
    serializer_class = CPU_IDs_Serializer

    def get_queryset(self):
        return CPU.objects.all().order_by("-id")
