from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = [
            'id',
            'shift',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
