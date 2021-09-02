from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # SAFE_METHODS is a Read-only to other objects
        if request.method in permissions.SAFE_METHODS:

            return True

        """
        Object.id == user.id ? authorize : un-authorize to permissions*reading
        """
        return obj.id == request.user.id
