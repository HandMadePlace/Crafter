from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import CrafterPerson


class CrafterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return CrafterPerson.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()

        return instance
