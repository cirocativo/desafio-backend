from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField()
    owner = serializers.CharField()