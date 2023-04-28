from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    
    profile_pic = models.ImageField(
        blank=True,
        null=True,
        upload_to="profile_pics",
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Doctor(models.Model):
    doctor = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
    )

    license_pic = models.ImageField(
        blank=True,
        null=True,
        upload_to="license_pic",
    )

    def __str__(self):
        return self.doctor.username
    
@receiver(post_save, sender=Doctor)
def update_doctor_status(sender, instance, **kwargs):
    if instance.license_pic:
        instance.doctor.is_doctor = True
    else:
        instance.doctor.is_doctor = False
    instance.doctor.save()


class Patient(models.Model):
    patient = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.patient.username

