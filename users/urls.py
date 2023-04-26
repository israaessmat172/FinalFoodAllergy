from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DoctorRegistrationView,
                    FacebookLogin,GitHubLogin, PatientRegistrationView, TwitterLogin, CustomLoginView,)

urlpatterns = [
    path("api/facebook/", FacebookLogin.as_view(), name="fb_login"),
    path("api/twitter/", TwitterLogin.as_view(), name="twitter_login"),
    path("api/github/", GitHubLogin.as_view(), name="github_login"),
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
