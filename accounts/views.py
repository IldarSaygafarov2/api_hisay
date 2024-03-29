import requests
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Category
from api.serializers import UserRequestSerializer
from api.utils import get_address_by_coordinates
from hisay import settings
from . import helpers
from .models import SimpleUserProfile, ServiceSetting
from .serializers import SimpleUserProfileSerializer, ServiceSettingsSerializer


@api_view(['POST'])
def save_user(request):
    data = request.data
    user = SimpleUserProfile.objects.filter(
        phone_number=data['phone_number']
    ).first()
    if user is None:
        return Response({"status": False})

    user.fullname = data['fullname']
    user.is_service = data['is_service']

    user.save()

    code = helpers.generate_code()
    user.verification_code = code
    user.save()

    # helpers.send_sms_code(data, code)
    requests.post(url=settings.telegram_msg_url.format(
        token=settings.BOT_TOKEN,
        chat_id=user.tg_chat_id,
        text=code
    ))
    return Response({
        "status": True,
        "id": user.pk
    })


@api_view(['POST'])
def save_data_from_bot(request):
    data = {k: v[0] for k, v in dict(**request.data).items()}
    try:
        user = SimpleUserProfile.objects.create(**data)
        user.save()
    except Exception as e:
        print(e)
        return Response({"status": "error"})
    return Response({"status": "ok"})


@api_view(["POST"])
def check_verification_code(request):
    data = request.data
    user = SimpleUserProfile.objects.filter(
        verification_code=data['verification_code'])
    if not user:
        return Response({"status": False})
    return Response({'status': True, "user_id": user.first().pk})


@api_view(['POST'])
def login_user(request):
    data = request.data
    phone_number = data['phone_number']
    user = SimpleUserProfile.objects.filter(phone_number=phone_number).first()
    if user is None:
        return Response({"status": False})

    code = helpers.generate_code()
    user.verification_code = code
    user.save()

    requests.post(url=settings.telegram_msg_url.format(
        token=settings.BOT_TOKEN,
        chat_id=user.tg_chat_id,
        text=code
    ))
    return Response({
        "status": True,
        "id": user.pk,
        "fullname": user.fullname
    })


@api_view(["GET"])
def get_user(request, pk):
    user = SimpleUserProfile.objects.filter(pk=pk).first()
    if user is None:
        return Response({"status": False})

    data = {
        "id": user.pk,
        "tg_username": user.tg_username,
        "tg_chat_id": user.tg_chat_id,
        "fullname": user.fullname.title(),
        "phone_number": user.phone_number,
        "rating": user.rating,
        "is_service": user.is_service,
        "is_banned": user.is_banned,
        "user_avatar": user.user_avatar.url if user.user_avatar else ""
    }
    return Response(data)


@api_view(["POST"])
def switch_user(request):
    data = request.data
    services_settings = ServiceSetting.objects.all()

    user = SimpleUserProfile.objects.filter(
        phone_number=data["phone_number"]).first()
    if user is None:
        return Response({"status": False})

    user.is_service = data['is_service']
    user.save()

    if user.is_service:
        service_settings = ServiceSetting.objects.filter(service_profile=user).first()
        if service_settings is None:
            obj = ServiceSetting.objects.create(
                service_profile=user
            )
            obj.save()
    return Response({"status": True})


class UpdateSimpleUser(generics.UpdateAPIView):
    serializer_class = SimpleUserProfileSerializer
    queryset = SimpleUserProfile.objects.all()


@api_view(["GET"])
def get_services(request):
    users = SimpleUserProfile.objects.filter(is_service=True)
    serializer = SimpleUserProfileSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_user_requests(request, pk):
    user = SimpleUserProfile.objects.filter(pk=pk).first()
    if user is None:
        return Response({"status": False})

    user_requests = user.user_requests.all()
    serializer = UserRequestSerializer(user_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_service_setting(request, service_id):
    service = SimpleUserProfile.objects.get(pk=service_id)
    setting = ServiceSetting.objects.filter(service_profile=service.pk).first()
    serializer = ServiceSettingsSerializer(setting, many=False)
    return Response(serializer.data)


class ServiceSettingRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = ServiceSetting.objects.all()
    serializer_class = ServiceSettingsSerializer
    lookup_field = 'service_profile_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        data = request.data

        # objects
        category = Category.objects.get(name=request.data.get('category'))
        service_profile = SimpleUserProfile.objects.get(pk=data.get('service_profile'))
        address = get_address_by_coordinates(data.get('location')) if data.get('location') else ''

        # updating
        instance.address_by_location = address
        instance.service_profile = service_profile
        instance.passport_series = data.get('passport_series')
        instance.passport_number = data.get('passport_number') if data.get('passport_number') else 0
        instance.hashtags = data.get('hashtags')
        instance.category = category
        instance.education = data.get('education')
        instance.location = data.get('location')
        instance.save()
        serializer = ServiceSettingsSerializer(instance, many=False)
        return Response(serializer.data)
