from rest_framework import serializers
from .models import ParkingLot
from accounts.serializers import AccountSerializer


class ParkingLotSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingLot
        fields = ['id', 'name', 'account']
        fields = '__all__'
        # depth = 1
