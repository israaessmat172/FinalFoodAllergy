from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import (DoctorRegistrationView,
                    FacebookLogin,GitHubLogin, PatientRegistrationView, TwitterLogin, CustomLoginView,UserProfileViewSet)


from dj_rest_auth.views import (
    PasswordResetConfirmView,
    PasswordResetView,
)

urlpatterns = [
    # other URL patterns here...
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/passwordd/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
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
router.register('user-profile', UserProfileViewSet, basename='user-profile')
urlpatterns = [
    path("", include(router.urls)),
    path("loggin/", CustomLoginView.as_view(), name="login"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
