from django.db.models import Q
from django.shortcuts import redirect, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import SimpleUserProfile as User
from .models import Conversation
from .serializers import ConversationListSerializer, ConversationSerializer


# Create your views here.
@api_view(['POST'])
def start_convo(request, ):
    data = request.data
    username = data.pop('username1')
    username2 = data.pop('username2')
    try:
        participant = User.objects.get(tg_username=username)
        participant2 = User.objects.get(tg_username=username2)

    except User.DoesNotExist:
        return Response({'message': 'You cannot chat with a non existent user'})

    conversation = Conversation.objects.filter(Q(initiator=participant2, receiver=participant) |
                                               Q(initiator=participant, receiver=participant2))
    if conversation.exists():
        return redirect(reverse('get_conversation', args=(conversation[0].id,)))
    else:
        conversation = Conversation.objects.create(initiator=participant2, receiver=participant)
        return Response(ConversationSerializer(instance=conversation).data)


@api_view(['GET'])
def get_conversation(request, convo_id):
    conversation = Conversation.objects.filter(id=convo_id)
    if not conversation.exists():
        return Response({'message': 'Conversation does not exist'})
    else:
        serializer = ConversationSerializer(instance=conversation[0])
        return Response(serializer.data)


@api_view(['GET'])
def conversations(request):
    username = request.GET.get('username')
    user = User.objects.get(tg_username=username)
    conversation_list = Conversation.objects.filter(Q(initiator=user) |
                                                    Q(receiver=user))
    serializer = ConversationListSerializer(instance=conversation_list, many=True)
    return Response(serializer.data)
