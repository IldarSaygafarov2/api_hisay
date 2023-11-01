from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, QuestionAnswer, ImageItem, UserRequest, Story, CategoryHashtag
from .serializers import (
    CategorySerializer,
    QuestionAnswerSerializer,
    ImageItemSerializer,
    UserRequestSerializer,
    StorySerializer
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoryListView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def list(self, request, *args, **kwargs):
        result = []
        for item in self.get_queryset():
            obj = {
                "pk": item.pk,
                "preview": item.preview.url if item.preview else '',
                "images": [
                    img.image.url for img in item.storyimage_set.all()
                ]
            }
            result.append(obj)
        return Response(result)


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

    def create(self, request, *args, **kwargs):
        data = request.data
        category = Category.objects.get(name=data.get('category'))
        hashtags = list(set(data.get("hashtags").split(', ')))

        for tag in hashtags:
            item = CategoryHashtag.objects.create(
                category=category,
                tag=tag
            )
            item.save()

        return super().create(request, *args, **kwargs)


class UserRequestRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    def get(self, request, *args, **kwargs):
        queryset = UserRequest.objects.filter(pk=kwargs['pk']).first()
        if queryset is None:
            return Response({"status": False})
        ser = UserRequestSerializer(queryset, many=False)
        return Response(ser.data)


class UserRequestDeleteView(generics.DestroyAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


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
