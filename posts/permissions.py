from rest_framework import permissions
from users.models import Doctor
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsDoctor(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        if request.user.is_patient:
            raise PermissionDenied(self.message)
        return request.user.doctor is not None

# class IsDoctorOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow doctors to create comments.
#     """
#     def has_permission(self, request, view):
#         # Allow read-only access to everyone
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Only allow doctors to create comments
#         return request.user.doctor_profile is not None


# class IsDoctor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.doctor is not None
        
class IsDoctorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow doctors to create comments.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return request.user.doctor_profile is not None
        except Doctor.DoesNotExist:
            return False
        
class IsDoctorOrPatientOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow doctors and patients to create posts and likes.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.doctor_profile is not None or request.user.patient_profile is not None)
