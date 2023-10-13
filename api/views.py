from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


class UserRequestRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


@api_view(["GET"])
def get_requests_by_category(request, category_id):
    category = Category.objects.filter(pk=category_id).first()
    if category is None:
        return Response({"status": False})

    user_requests = UserRequest.objects.filter(category=category)
    serializer = UserRequestSerializer(user_requests, many=True)
    return Response(serializer.data)
