from rest_framework import serializers
from configurator.models import Configurator
# from cpu.api.serializers import (CPUSerializer,
#                                  CPU_IDs_Serializer)
# from graphic_card.api.serializers import (Graphic_CardSerializers,
#                                           Graphic_Card_IDS_Serializers)
from software.api.serializers import (All_Games_Serializer,
                                      # All_Games_IDs_Serializer,
                                      All_OfficeWare_Serializer,
                                      # All_OfficeWare_IDs_Serializer,
                                      # All_Operating_System_Serializer,
                                      # All_Operating_System_IDs_Serializer
                                      )


class All_Configurator_Serializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)

    cpu = serializers.StringRelatedField()
    graphic_card = serializers.StringRelatedField()
    operating_system = serializers.StringRelatedField()

    games = serializers.SerializerMethodField()
    officeware = serializers.SerializerMethodField()

    class Meta:
        model = Configurator
        fields = '__all__'

        def get_officeware(self, instance):
            officeware_serializer = All_OfficeWare_Serializer(instance.configurations, many=True)
            return officeware_serializer.data

        def get_games(self, instance):
            games_serializer = All_Games_Serializer(instance.configurations, many=True)
            return games_serializer.data


class All_Configurator_IDs_Serializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)
    cpu_id = serializers.PrimaryKeyRelatedField(read_only=True)
    graphic_card_id = serializers.PrimaryKeyRelatedField(read_only=True)
    operating_system_id = serializers.PrimaryKeyRelatedField(read_only=True)
    games_ids = serializers.SerializerMethodField()
    officeware_ids = serializers.SerializerMethodField()

    class Meta:
        model = Configurator
        fields = ['id']

    def get_games_ids(self, instance):
        return [game.id for game in list(instance.games.all())]

    def get_officeware_ids(self, instance):
        return [officeware.id for officeware in list(instance.officewares.all())]


class Users_Configurator_Serializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)
    cpu = serializers.StringRelatedField()
    graphic_card = serializers.StringRelatedField()
    operating_system = serializers.StringRelatedField()
    games = serializers.SerializerMethodField()
    officeware = serializers.SerializerMethodField()

    class Meta:
        model = Configurator
        fields = '__all__'

    def get_games(self, instance):
        games_serializer = All_Games_Serializer(instance.configurations, many=True)
        return games_serializer.data

    def get_officeware(self, instance):
        officeware_serializer = All_OfficeWare_Serializer(instance.configurations, many=True)
        return officeware_serializer.data


class Users_Configurator_IDs_Serializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(read_only=True)
    cpu_id = serializers.StringRelatedField()
    graphic_card_id = serializers.StringRelatedField()
    operating_system_id = serializers.StringRelatedField()
    games_ids = serializers.SerializerMethodField()
    officeware_ids = serializers.SerializerMethodField()

    class Meta:
        model = Configurator
        fields = ['id']

    def get_games_ids(self, instance):
        return [game.id for game in list(instance.games.all())]

    def get_officeware_ids(self, instance):
        return [officeware.id for officeware in list(instance.officewares.all())]
