from rest_framework import serializers

from api.utils import get_address_by_coordinates
from .models import SimpleUserProfile, ServiceSetting
from api.models import Category


class ServiceSettingsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        read_only=False,
        slug_field='name'
    )

    class Meta:
        model = ServiceSetting
        fields = [
            'pk',
            'service_profile',
            'passport_series',
            'passport_number',
            'hashtags',
            'category',
            'education',
            'location',
            'address_by_location'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get("address_by_location"):
            data['address_by_location'] = get_address_by_coordinates(data.get("location"))
        return data


class SimpleUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ['pk', 'fullname', 'is_service', 'city',
                  'education', 'info_about', 'user_avatar']


class ServiceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ['pk', 'fullname', 'tg_username', 'rating', 'education', 'education', 'info_about', 'city']