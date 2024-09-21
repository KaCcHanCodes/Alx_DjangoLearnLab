from .models import Notification
from rest_framework import permissions, generics
from .serializers import NotificationSerializer

class NotificationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        # Fetch notifications for the authenticated user and order by unread notifications
        return Notification.objects.filter(receipient=self.request.user).order_by('-is_read')