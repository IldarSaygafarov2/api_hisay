from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, QuestionAnswer, ImageItem, UserRequest
from .serializers import CategorySerializer, QuestionAnswerSerializer, ImageItemSerializer, UserRequestSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryRetrieveView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         category = Category.objects.get(pk=kwargs['category_id'])
#         user_requests = UserRequest.objects.filter(category=category)
#         serializer = UserRequestSerializer(user_requests, many=True)
#         return Response(serializer.data)


class QuestionAnswerList(generics.ListAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


class ImageItemList(generics.ListAPIView):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer


class UserRequestCreateListView(generics.ListCreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    def list(self, request, *args, **kwargs):
        queryset = UserRequest.objects.all()
        ser = UserRequestSerializer(queryset, many=True)
        return Response(ser.data)


class UserRequestRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    def get(self, request, *args, **kwargs):
        queryset = UserRequest.objects.get(pk=kwargs['pk'])
        ser = UserRequestSerializer(queryset, many=False)
        return Response(ser.data)




@api_view(["GET"])
def get_requests_by_category(request, category_id):
    category = Category.objects.filter(pk=category_id).first()
    if category is None:
        return Response({"status": False})

    user_requests = UserRequest.objects.filter(category=category)

    serializer = UserRequestSerializer(user_requests, many=True)
    print(request.META)
    print(request.META['HTTP_HOST'])
    return Response(serializer.data)
