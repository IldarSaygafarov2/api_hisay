import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hisay import settings
from . import helpers
from .models import SimpleUserProfile


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

    requests.post(url=settings.telegram_msg_url.format(
        token=settings.BOT_TOKEN,
        chat_id=user.tg_chat_id,
        text=code
    ))
    return Response({
        "status": True
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
    user = SimpleUserProfile.objects.filter(verification_code=data['verification_code'])
    if not user:
        return Response({"status": False})
    return Response({'status': True, "user_id": user.first().pk})


