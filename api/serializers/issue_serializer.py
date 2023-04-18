from rest_framework import serializers

from api.serializers.project_serializer_for_issue import ProjectsForIssuesSerializer
from api.serializers.status_serializer import StatusSerializer
from api.serializers.type_serializer import TypeSerializer
from issue_tracker.models import Issue


class IssuesForProjectsSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "summary",
            "description",
            "status",
            "type",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_at",
            "project",
        ]
        read_only_fields = [
            "id",
            "type",
            "created_ad",
            "updates_at",
            "is_deleted",
            "deleted_at",
            "project",
        ]


class IssuesSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(many=True, read_only=True)
    project = ProjectsForIssuesSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "summary",
            "description",
            "status",
            "type",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_at",
            "project",
        ]
        read_only_fields = [
            "id",
            "type",
            "created_ad",
            "updates_at",
            "is_deleted",
            "deleted_at",
            "project",
        ]
