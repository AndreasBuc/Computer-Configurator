from graphic_card.models import Grafic_Card
from rest_framework import serializers


class Graphic_CardSerializers(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    name = serializers.SerializerMethodField()

    class Meta:
        model = Grafic_Card
        fields = '__all__'

    def get_name(self, instance):
        return f'{instance.manufacturer} {instance.model}'


class Graphic_Card_IDS_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Grafic_Card
        fields = ['id']
