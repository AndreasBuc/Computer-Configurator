from rest_framework import permissions


class IsAdminCreatorOrReadOnly(permissions.BasePermission):
    """
    Should only be editable by an Admin, Creator, else read only
    """
    message = 'Adding is only permitted by Admins or the Creator'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user or request.user.is_staff
