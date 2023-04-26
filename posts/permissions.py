from rest_framework import permissions
from users.models import Doctor

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
