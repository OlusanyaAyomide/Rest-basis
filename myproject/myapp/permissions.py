from rest_framework import permissions

class ReviewEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.review_user == request.user:
                return True
            else:
                return False