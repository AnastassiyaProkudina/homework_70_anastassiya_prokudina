from rest_framework import serializers

from api.serializers.issue_serializer import IssuesForProjectsSerializer
from api.serializers.user_serializer import UsersSerializer
from issue_tracker.models import Project


class ProjectsSerializer(serializers.ModelSerializer):
    issues = IssuesForProjectsSerializer(many=True, read_only=True)
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
            "issues",
        ]
        read_only_fields = ["id", "is_deleted", "deleted_at", "users", "issues"]

