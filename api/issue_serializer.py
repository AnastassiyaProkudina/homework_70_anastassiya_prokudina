from rest_framework import serializers

from issue_tracker.models import Issue


class IssuesBaseSerializer(serializers.ModelSerializer):
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
