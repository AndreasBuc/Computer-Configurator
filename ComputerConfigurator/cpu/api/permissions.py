from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminCreatorOrReadOnly(permissions.BasePermission):
    """
    Should only be editable by an Admin, Creator, else read only
    """
    message = 'Editing is only permitted by Admins or the Creator'

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user or request.user.is_staff
