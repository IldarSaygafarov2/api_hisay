import requests
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hisay import settings
from . import helpers
from .models import SimpleUserProfile
from .serializers import SimpleUserProfileSerializer
from api.serializers import UserRequestSerializer


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
    except:
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
    user = SimpleUserProfile.objects.filter(
        phone_number=data["phone_number"]).first()
    if user is None:
        return Response({"status": False})

    user.is_service = data['is_service']
    user.save()
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
