from rest_framework import generics

from .models import Category, QuestionAnswer, ImageItem, UserRequest
from .serializers import CategorySerializer, QuestionAnswerSerializer, ImageItemSerializer, UserRequestSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerList(generics.ListAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


class ImageItemList(generics.ListAPIView):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer


class UserRequestCreateListView(generics.ListCreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
