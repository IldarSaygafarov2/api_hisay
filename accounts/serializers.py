from rest_framework import serializers
from .models import SimpleUserProfile


class SimpleUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ['pk', 'fullname', 'city',
                  'education', 'info_about', 'user_avatar']
