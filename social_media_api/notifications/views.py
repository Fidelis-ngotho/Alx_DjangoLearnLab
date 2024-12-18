from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        unread_notifications = notifications.filter(read=False)
        serialized_notifications = [
            {
                "id": notification.id,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.timestamp,
                "read": notification.read
            } for notification in notifications
        ]
        return Response(serialized_notifications)

    def post(self, request):
        notifications = request.user.notifications.filter(read=False)
        notifications.update(read=True)
        return Response({"detail": "All notifications marked as read."})

# Create your views here.
