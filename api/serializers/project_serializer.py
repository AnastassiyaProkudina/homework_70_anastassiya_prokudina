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


# class ProjectsForIssuesSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200, min_length=5, required=True, allow_blank=True)
#     description = serializers.CharField(max_length=1000, required=True, allow_blank=True)
#     is_deleted = serializers.BooleanField(required=True, read_only=True)
#     deleted_at = serializers.DateTimeField(read_only=True)
#     users = UsersSerializer(many=True, read_only=True)

    # class Meta:
    #     model = Project
    #
    #     fields = [
    #         "id",
    #         "title",
    #         "description",
    #         "is_deleted",
    #         "deleted_at",
    #         "users",
    #     ]
    #     read_only_fields = ["id", "is_deleted", "deleted_at", "users"]
