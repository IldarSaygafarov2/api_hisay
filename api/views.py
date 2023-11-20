from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import SimpleUserProfile
from .models import Category, QuestionAnswer, ImageItem, UserRequest, Story, CategoryHashtag, ServiceUserRequestResponse
from .serializers import (
    CategorySerializer,
    QuestionAnswerSerializer,
    ImageItemSerializer,
    UserRequestSerializer,
    StorySerializer,
    ServiceUserRequestResponseSerializer
)
from .utils import get_address_by_coordinates


class ServiceUserRequestResponseList(generics.ListCreateAPIView):
    queryset = ServiceUserRequestResponse.objects.all()
    serializer_class = ServiceUserRequestResponseSerializer


class ServicesRespondedToUserRequest(generics.RetrieveAPIView):
    queryset = ServiceUserRequestResponse.objects.all()
    serializer_class = ServiceUserRequestResponseSerializer

    def retrieve(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(user_request=kwargs['pk'])
        services_ids = list(set([i.service.pk for i in qs]))
        # TODO: получить данные про сервис и отдать



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
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
        query_params = self.request.query_params
        if query_params:
            queryset = UserRequest.objects.filter(hashtags__contains=query_params.get("hashtags"))
        else:
            queryset = UserRequest.objects.all()

        ser = UserRequestSerializer(queryset, many=True)
        return Response(ser.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        address = get_address_by_coordinates(data.get("location"))
        category = Category.objects.get(name=data.get('category'))
        profile = SimpleUserProfile.objects.get(pk=data.get('author'))
        hashtags = list(set(data.get("hashtags").split(', ')))

        data_dict = {k: data.get(k) for k in data.keys() if k != 'csrfmiddlewaretoken'}
        data_dict['category'] = category
        data_dict['location'] = address
        data_dict['author'] = profile

        for tag in hashtags:
            tag = tag.replace("#", "")
            item = CategoryHashtag.objects.create(
                category=category,
                tag=tag
            )
            item.save()

        new_request = UserRequest.objects.create(
            **data_dict
        )
        new_request.save()
        serializer = UserRequestSerializer(new_request, many=False)
        return Response(serializer.data)


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
    return Response(serializer.data)
