from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Only allow the User to see his/hers Configurations
    """

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_staff


class IsAdminCreatorOrReadOnly(permissions.BasePermission):
    """
    Should only be editable by an Admin, Creator, else read only
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user or request.user.is_staff
