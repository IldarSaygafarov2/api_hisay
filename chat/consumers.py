import json
from accounts.models import SimpleUserProfile
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message, Conversation
from .serializers import MessageSerializer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("here")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        print("here2")
        self.accept()
        print("here3")

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        # parse the json data into dictionary object
        text_data_json = json.loads(text_data)

        # unpack the dictionary into the necessary parts
        message = text_data_json["message"]

        conversation = Conversation.objects.get(id=int(self.room_name))
        # print(self.scope['query_string'].decode().split('=')[-1])
        # # sender = self.scope["user"]
        sender = SimpleUserProfile.objects.get(tg_username=self.scope['query_string'].decode().split('=')[-1])

        _message = Message.objects.create(
            sender=sender,
            text=message,
            conversation_id=conversation,
        )
        # Send message to room group
        chat_type = {"type": "chat_message"}
        message_serializer = (dict(MessageSerializer(instance=_message).data))
        return_dict = {**chat_type, **message_serializer}
        # if _message.attachment:
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.room_group_name,
        #         {
        #             "type": "chat_message",
        #             "message": message,
        #             "sender": sender.email,
        #             "time": str(_message.timestamp),
        #         },
        #     )
        # else:
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            return_dict,
        )

    # Receive message from room group
    def chat_message(self, event):
        dict_to_be_sent = event.copy()
        dict_to_be_sent.pop("type")

        # Send message to WebSocket
        self.send(
            text_data=json.dumps(
                dict_to_be_sent
            )
        )
