from rest_framework import generics

from .models import Category, QuestionAnswer, ImageItem
from .serializers import CategorySerializer, QuestionAnswerSerializer, ImageItemSerializer



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerList(generics.ListAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


class ImageItemList(generics.ListAPIView):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer

