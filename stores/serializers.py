from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    owner = serializers.CharField()