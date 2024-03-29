from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissions are only allowed to the owner of the snippet. 
        if not request.user.is_anonymous:
            return request.user == obj
        
        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user