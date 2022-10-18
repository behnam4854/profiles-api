from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profiles"""
    def has_object_permission(self, request, view, obj):
        """check if user have the permission to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """allowing the user for updating thier own status"""
    def has_object_permission(self, request, view, obj):
        """check if the user is trying to view his of hers status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id