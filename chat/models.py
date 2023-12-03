from django.db import models
from django.conf import settings
from accounts.models import SimpleUserProfile


# Create your models here.

class Conversation(models.Model):
    initiator = models.ForeignKey(
        SimpleUserProfile, on_delete=models.SET_NULL, related_name="convo_starter", null=True
    )
    receiver = models.ForeignKey(
        SimpleUserProfile, on_delete=models.SET_NULL, related_name="convo_participant", null=True
    )
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(SimpleUserProfile, on_delete=models.SET_NULL,
                               related_name='message_sender', null=True)
    text = models.CharField(max_length=200)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)