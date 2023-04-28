from django.db import models


class ParkingLot(models.Model):
    name = models.CharField(max_length=255)

    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='parking_lots'
        )
