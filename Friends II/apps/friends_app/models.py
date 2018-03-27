from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..PBT_app.models import User 


class FriendManager(models.Manager):
    def newFriend(self, user_id, friend_id):
        sender = User.objects.get(id=user_id)
        receiver = User.objects.get(id=friend_id)
        Friend.objects.create(user=sender, friend=receiver)
        Friend.objects.create(user=receiver, friend=sender)

    def removeFriend(self, user_id, friend_id):
        sender = User.objects.get(id=user_id)
        receiver = User.objects.get(id=friend_id)
        Friend.objects.get(user=sender, friend=receiver).delete()
        Friend.objects.get(user=receiver, friend=sender).delete()


class Friend(models.Model):
    user = models.ForeignKey(User, related_name="sender2")
    friend = models.ForeignKey(User, related_name="receiver2")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = FriendManager()
# Create your models here.
