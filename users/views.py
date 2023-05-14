from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from rest_framework import  viewsets
from rest_framework.response import Response
from .serializers import (
    CustomPatientRegistrationSerializer,
    DoctorCustomRegistrationSerializer,
    DetailedTokenSerializer,
    UserProfileSerializer,
)
from .models import User, Doctor
from .serializers import LicenseSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
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

class UserProfileViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, pk=None):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "CALLBACK_URL_YOU_SET_ON_GITHUB"
    client_class = OAuth2Client

class LicenseView(viewsets.ModelViewSet):
    serializer_class = LicenseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user=request.user
        data=request.data
        ser= self.serializer_class(**data)
        if ser.is_valid():
            user.is_doctor=True
            user.save()
            doctor=Doctor