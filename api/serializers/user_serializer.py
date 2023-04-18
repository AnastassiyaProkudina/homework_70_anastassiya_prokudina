from rest_framework import serializers


class UsersSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True, allow_blank=True)
    last_name = serializers.CharField(max_length=200, required=True, allow_blank=True)
    username = serializers.CharField(max_length=200, required=True, allow_blank=True)
