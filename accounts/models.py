from django.db import models


# Create your models here.


class SimpleUserProfile(models.Model):
    tg_username = models.CharField(max_length=150, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    tg_chat_id = models.BigIntegerField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    is_service = models.BooleanField(default=False, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.fullname}: {self.phone_number}"
