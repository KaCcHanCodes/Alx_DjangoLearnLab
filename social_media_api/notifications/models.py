from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notif_receiver')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notif_sender')

    ACTIONS = [
        ('Like', 'notification on new post like'),
        ('Follow', 'notification on new following'),
        ('Comment', 'notifications on post comments'),
        ('Post', 'notifications on new post')
    ]

    verb = models.CharField(max_length=15, choices=ACTIONS, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='notifications', blank=True)
    object_id = models.PositiveIntegerField(blank=True)
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb} for {self.recipient}"