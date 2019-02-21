from rest_framework.permissions import BasePermission

class IsUserAdd(BasePermission):
    message = "You are not the one who add the item. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.added_by:
            return True
        return False