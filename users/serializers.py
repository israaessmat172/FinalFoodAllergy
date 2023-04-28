from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from .models import  Doctor, Patient

class LoginSerializer(LoginSerializer):
    username = None


from dj_rest_auth.serializers import TokenSerializer

class DetailedTokenSerializer(TokenSerializer):
    status = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()

    id = serializers.IntegerField(source="user.id")
    name = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    phone = serializers.CharField(source="user.phone")
    image = serializers.ImageField(source="user.profile_pic")
    is_doctor = serializers.BooleanField(source="user.is_doctor")
    
    token = serializers.CharField(source="key")
    
    class Meta(TokenSerializer.Meta):
        fields = ["status", "message", "id", "name", "email","phone", "image", "is_doctor", "token"]
    
    def get_status(self, obj):
        return True if obj else False

    def get_message(self, obj):
        return "تم تسجيل الدخول بنجاح" if obj else "خطأ في البريد الالكتروني او كلمة المرور"

class DoctorCustomRegistrationSerializer(RegisterSerializer):
    phone = serializers.CharField(required=True)

    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        print(data)
        extra_data = {
            "phone": self.validated_data.get("phone", ""),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        data = self.get_cleaned_data()
        phone = data.get("phone")

        user = super().save(request)
        # user.is_doctor = True
        user.phone = phone
        user.save()
        
        doctor = Doctor(doctor=user)

        doctor.save()

        return user


class CustomPatientRegistrationSerializer(RegisterSerializer):
    phone = serializers.CharField(required=True)

    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    def get_cleaned_data(self):
        data = super().get_cleaned_data()

        extra_data = {
            "phone": self.validated_data.get("phone", ""),
        }
    
        data.update(extra_data)
        return data

    def save(self, request):
        data = self.get_cleaned_data()

        phone = data.get("phone")
        
        user = super().save(request)
        user.is_patient = True
        user.phone = phone
        
        user.save()

        patient = Patient(
            patient=user,
        )
        patient.save()
        return user
