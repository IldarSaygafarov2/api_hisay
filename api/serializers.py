from rest_framework import serializers

from .models import Category, QuestionAnswer, ImageItem, UserRequest


class CategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Category
        fields = ['pk', 'name', "icon", 'subcategories']


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['pk', 'question', 'answer']


class ImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageItem
        fields = ['pk', 'photo']


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['pk', 'body', 'location', 'price', 'photo', 'hashtags', 'category', 'author']
