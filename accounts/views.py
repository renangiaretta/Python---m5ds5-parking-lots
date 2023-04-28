from .serializers import AccountSerializer
from .models import Account
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOwner
from drf_spectacular.utils import extend_schema


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        operation_id='accounts_list',
        responses={200: AccountSerializer},
        description='Rota Listagem de Contas.',
        summary='Sumário Listagem de Contas.',
        tags=['Tag Listagem de Contas']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = 'account_id'
