from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import CrafterPerson


class CrafterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField()
