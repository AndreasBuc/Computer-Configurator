from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from configurator.models import Configurator
from configurator.api.serializers import (All_Configurator_Serializer,
                                          All_Configurator_IDs_Serializer)
from configurator.api.permissions import IsOwnerOrAdmin
from software.models import Games, OfficeWare


class All_Configurator_Viewset(viewsets.ModelViewSet):
    serializer_class = All_Configurator_Serializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Configurator.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class All_Configurator_Ids_Viewset(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = All_Configurator_IDs_Serializer

    def get_queryset(self):
        return Configurator.objects.all().order_by("-id")


class Users_Configurator_Viewset(viewsets.ModelViewSet):
    serializer_class = All_Configurator_Serializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Configurator.objects.all().filter(creator_id=self.request.user.id).order_by("-id")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class Users_Configurator_Ids_Viewset(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = All_Configurator_IDs_Serializer

    def get_queryset(self):
        return Configurator.objects.all().filter(creator_id=self.request.user.id).order_by("-id")


class Users_Configurator_Add_Remove_Game_APIView(APIView):
    serializer_class = All_Configurator_Serializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Configurator.objects.all().filter(owner_id=self.request.user.id).order_by("name")

    def delete(self, request, g_pk, c_pk):
        """Remove this Game from Configurator"""

        configurator = get_object_or_404(Configurator, pk=c_pk)
        if not (configurator.creator == request.user or request.user.is_staff):
            return Response({'error': 'You have no permissions'}, status=status.HTTP_403_FORBIDDEN)
        game = get_object_or_404(Games, pk=g_pk)
        configurator.games.remove(game)
        configurator.save()
        print(f'Delete method: request: {request.data}')
        serializer_context = {"request": request}
        serializer = self.serializer_class(configurator, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, g_pk, c_pk):
        """Add request.user to the voters queryset of an answer instance."""
        configurator = get_object_or_404(Configurator, pk=c_pk)
        if not (configurator.creator == request.user or request.user.is_staff):
            return Response({'error': 'You have no permissions'}, status=status.HTTP_403_FORBIDDEN)
        game = get_object_or_404(Games, pk=g_pk)
        configurator.games.add(game)
        print(f'Post method: request: {request.data}')
        configurator.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(configurator, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Users_Configurator_Add_Remove_OfficeWare_APIView(APIView):
    serializer_class = All_Configurator_Serializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Configurator.objects.all().filter(owner_id=self.request.user.id).order_by("name")

    def delete(self, request, o_pk, c_pk):
        """Remove this officeware from Configurator"""
        configurator = get_object_or_404(Configurator, pk=c_pk)
        if not (configurator.creator == request.user or request.user.is_staff):
            return Response({'error': 'You have no permissions'}, status=status.HTTP_403_FORBIDDEN)
        officeware = get_object_or_404(OfficeWare, pk=o_pk)
        configurator.officewares.remove(officeware)
        configurator.save()
        print(f'Delete method: request: {request.data}')
        serializer_context = {"request": request}
        serializer = self.serializer_class(configurator, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, o_pk, c_pk):
        """Add officeware to configuration"""
        configurator = get_object_or_404(Configurator, pk=c_pk)
        if not (configurator.creator == request.user or request.user.is_staff):
            return Response({'error': 'You have no permissions'}, status=status.HTTP_403_FORBIDDEN)
        officeware = get_object_or_404(OfficeWare, pk=o_pk)
        configurator.officewares.add(officeware)
        print(f'Post method: request: {request.data}')
        configurator.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(configurator, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
