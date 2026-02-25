from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
   def  has_object_permission(self, request, view, obj):
      return request.user.role == 'admin' or obj.user == request.user
   


class IsAuthorOrReadOnly(permissions.BasePermission):
   def  has_permission(self, request, view):
      if view.action== 'create':
         return request.user.is_authenticated and request.user.role=='author'
      return True 
   
   def  has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
         return True
      
      return obj.author ==request.user