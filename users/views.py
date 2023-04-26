from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from rest_framework import  viewsets
from .serializers import (
    CustomPatientRegistrationSerializer,
    DoctorCustomRegistrationSerializer,
    DetailedTokenSerializer,
)
# Create your views here.

    # Create your views here.

# ovveride LoginView dj_rest_auth login view to add data to Response body
from dj_rest_auth.views import LoginView

class CustomLoginView(LoginView):
    def get_response_serializer(self):
        return DetailedTokenSerializer

class DoctorRegistrationView(RegisterView, viewsets.GenericViewSet):
    serializer_class = DoctorCustomRegistrationSerializer


class PatientRegistrationView(RegisterView, viewsets.GenericViewSet):
    serializer_class = CustomPatientRegistrationSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "CALLBACK_URL_YOU_SET_ON_GITHUB"
    client_class = OAuth2Client