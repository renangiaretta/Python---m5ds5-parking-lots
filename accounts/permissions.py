from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Account


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(
        serlf, request: Request, view: View, obj: Account
    ) -> bool:
        return super().has_object_permission(request, view, obj)
