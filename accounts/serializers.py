from rest_framework import serializers
from .models import SimpleUserProfile


class SimpleUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ['pk', 'fullname', 'is_service', 'city',
                  'education', 'info_about', 'user_avatar']


class ServiceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ['pk', 'fullname', 'tg_username', 'rating', 'education', 'education', 'info_about', 'city']