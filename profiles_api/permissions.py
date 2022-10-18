from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profiles"""
    def has_object_permission(self, request, view, obj):
        """check if user have the permission to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
