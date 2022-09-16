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

class WatchAddPermission(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            print("safe")
            return True
        else:
            if request.user.is_staff:
                print("staff")
                return True
            else:
                print("non staff")
                return False
          