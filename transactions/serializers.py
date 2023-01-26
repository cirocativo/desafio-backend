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

    store = StoreSerializer(write_only=True)

    type_description = serializers.SerializerMethodField()

    def get_type_description(self, obj: Transaction) -> str:
        transaction_types_descriptions = [
            'débito',
            'boleto',
            'financiamento',
            'crédito',
            'recebimento empréstimo',
            'vendas',
            'recebimento TED',
            'recebimento DOC',
            'aluguel'
        ]

        transaction_type = int(obj.type_transaction) - 1

        return transaction_types_descriptions[transaction_type]

    def create(self, validated_data: dict):
        store_data = validated_data.pop('store')
        print(store_data)
        store, _ = Store.objects.get_or_create(**store_data, defaults={**store_data})

        transaction = Transaction.objects.create(**validated_data, store=store)

        return transaction