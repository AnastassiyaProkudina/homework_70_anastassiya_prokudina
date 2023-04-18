from rest_framework import serializers

from api.serializers.user_serializer import UsersSerializer
from issue_tracker.models import Project


class ProjectsForIssuesSerializer(serializers.ModelSerializer):
    users = UsersSerializer(many=True, read_only=True)

    class Meta:
        model = Project

        fields = [
            "id",
            "title",
            "description",
            "is_deleted",
            "deleted_at",
            "users",
        ]

        read_only_fields = ["id", "is_deleted", "deleted_at", "users"]
