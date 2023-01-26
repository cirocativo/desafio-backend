from rest_framework import serializers
from stores.serializers import StoreSerializer
from stores.models import Store
from .models import Transaction

class TransactionSerializer(serializers.Serializer):
    type_transaction = serializers.CharField()
    date = serializers.DateField()
    value = serializers.FloatField()
    cpf = serializers.CharField()
    card = serializers.CharField()
    hour = serializers.TimeField()

    store = StoreSerializer()

    def create(self, validated_data: dict):
        store_data = validated_data.pop('store')
        print(store_data)
        store, _ = Store.objects.get_or_create(**store_data, defaults={**store_data})

        transaction = Transaction.objects.create(**validated_data, store=store)

        return transaction