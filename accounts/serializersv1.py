from rest_framework import serializers
from .models import ShiftOptions, Account


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    shift = serializers.ChoiceField(
        choices=ShiftOptions.choices,
        default=ShiftOptions.DEFAULT,
    )
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=127)
    last_name = serializers.CharField(max_length=127)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if 'password' in validated_data:
            new_password = validated_data.pop('password')
            instance.set_password(new_password)
        instance.save()
        return instance
