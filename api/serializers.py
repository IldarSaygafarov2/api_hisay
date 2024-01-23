from rest_framework import serializers

from .models import Category, QuestionAnswer, ImageItem, UserRequest, Story, ServiceUserRequestResponse
from accounts.models import SimpleUserProfile


class ServiceUserRequestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUserRequestResponse
        fields = ['service', 'user_request']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['pk', 'preview']


class CategorySerializer(serializers.ModelSerializer):
    hashtags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="tag"
    )

    class Meta:
        model = Category
        fields = ['pk', 'name', "icon", 'hashtags']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['icon']:
            data['icon'] = ""
        return data


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['pk', 'question', 'answer']


class ImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageItem
        fields = ['pk', 'photo']


class UserRequestSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        read_only=False,
        slug_field='name'
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        author = SimpleUserProfile.objects.get(pk=data['author'])
        data['created_at'] = f'{instance.created_at.date()} {instance.created_at.strftime("%H:%M:%S")}'
        data['username'] = author.tg_username
        return data

    class Meta:
        model = UserRequest
        fields = [
            'pk',
            'title',
            'body',
            'location',
            'created_at',
            'photo',
            'photo2',
            'photo3',
            'photo4',
            'photo5',
            'photo6',
            'photo7',
            'photo8',
            'hashtags',
            'category',
            'author'
        ]
