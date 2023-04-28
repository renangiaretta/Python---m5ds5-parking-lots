from .serializers import AccountSerializer
from .models import Account
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOwner


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = 'account_id'
