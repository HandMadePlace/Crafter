from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import CrafterPerson


class CrafterSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = CrafterPerson
        fields = '__all__'
