from rest_framework import serializers
from cpu.models import CPU


class CPUSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    name = serializers.SerializerMethodField()

    class Meta:
        model = CPU
        fields = '__all__'

    def get_name(self, instance):
        return f'{instance.manufacturer} {instance.model}, {instance.kernel}x {instance.speed} GHz'


class CPU_IDs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = CPU
        fields = ['id']
