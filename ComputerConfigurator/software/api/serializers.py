from software.models import (Games, OfficeWare, Operating_System)

from rest_framework import serializers


class All_Games_Serializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Games
        fields = '__all__'
        read_only_fields = ['image']


class All_Games_IDs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = ['id']


class All_OfficeWare_Serializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OfficeWare
        fields = '__all__'


class All_OfficeWare_IDs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeWare
        fields = ['id']


class All_Operating_System_Serializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Operating_System
        fields = '__all__'


class All_Operating_System_IDs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Operating_System
        fields = ['id']


class GamesImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to games"""

    class Meta:
        model = Games
        fields = ('id', 'image')
        read_only_fields = ('id',)
