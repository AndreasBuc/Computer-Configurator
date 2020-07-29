from software.models import (Games, OfficeWare, Operating_System)
from software.api.serializers import (All_Games_Serializer,
                                      All_Games_IDs_Serializer,
                                      All_OfficeWare_Serializer,
                                      All_OfficeWare_IDs_Serializer,
                                      All_Operating_System_Serializer,
                                      All_Operating_System_IDs_Serializer,
                                      GamesImageSerializer)
from rest_framework import viewsets, status
from cpu.api.permissions import IsAdminCreatorOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class All_Games_ViewSet(viewsets.ModelViewSet):
    serializer_class = All_Games_Serializer
    permission_classes = [IsAdminCreatorOrReadOnly]

    def get_queryset(self):
        return Games.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'upload_image':
            return GamesImageSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a game"""
        if request.data["image"] == "":
            return Response({'message': 'You put no Image'}, status=status.HTTP_400_BAD_REQUEST)

        if str(request.data["image"]).split('.')[-1] not in 'jpg png bmp'.split():
            return Response({'message': 'The file is no Image, only accept jpg, png and bmp'}, status=status.HTTP_400_BAD_REQUEST)
        game = self.get_object()
        serializer = self.get_serializer(
            game,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class All_Games_IDs_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = All_Games_IDs_Serializer

    def get_queryset(self):
        return Games.objects.all().order_by("-id")


class All_OfficeWare_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = All_OfficeWare_Serializer

    def get_queryset(self):
        return OfficeWare.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_OfficeWare_IDs_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = All_OfficeWare_IDs_Serializer

    def get_queryset(self):
        return OfficeWare.objects.all().order_by("-id")


class All_Operating_System_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = All_Operating_System_Serializer

    def get_queryset(self):
        return Operating_System.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_Operating_System_IDs_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminCreatorOrReadOnly]
    serializer_class = All_Operating_System_IDs_Serializer

    def get_queryset(self):
        return Operating_System.objects.all().order_by("-id")
