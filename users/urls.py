from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DoctorRegistrationView,
                    FacebookLogin,GitHubLogin, PatientRegistrationView, TwitterLogin, CustomLoginView,)


from dj_rest_auth.views import (
    PasswordResetConfirmView,
    PasswordResetView,
)

urlpatterns = [
    # other URL patterns here...
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
]


app_name = "users"

router = DefaultRouter()

router.register(
    "registration/doctor",
    DoctorRegistrationView,
    basename="register-doctor",
)
router.register(
    "registration/patient",
    PatientRegistrationView,
    basename="register-patient",
)

urlpatterns = [
    path("", include(router.urls)),
    path("loggin/", CustomLoginView.as_view(), name="login"),
]
