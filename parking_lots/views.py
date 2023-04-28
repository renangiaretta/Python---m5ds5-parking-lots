from rest_framework import generics
from .models import ParkingLot
from .serializers import ParkingLotSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrParkingLotOwner


class ParkingLotView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(account=self.request.user)


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
    lookup_url_kwarg = 'id'
