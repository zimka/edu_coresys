import logging

from rest_framework import serializers, permissions
from django.conf import settings

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField()

    class Meta:
        model = Student
        exclude = ("id", "leader_id", "is_removed")


class ApiKeyPermission(permissions.BasePermission):
    """
    Разрешение по X-Api-Key в хедере
    """

    def has_permission(self, request, view):
        api_key = getattr(settings, 'API_KEY', None)
        if not api_key:
            logging.error('API_KEY not configured')
        if api_key is False:
            return True

        key = request.META.get('HTTP_X_API_KEY')
        if key and api_key and key == api_key:
            return True
        return False
