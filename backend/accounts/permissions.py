from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            # Allow GET requests without any restrictions
            return True
        elif request.method == 'POST' or request.method== 'PUT':
            # Add your custom logic for POST permissions here
            # For example, you can restrict POST to authenticated users:
            return request.user.is_authenticated
        else:
            # Deny other HTTP methods (PUT, DELETE, etc.) by default
            return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the post.
        return obj.user == request.user

