from rest_framework import serializers

from issue_tracker.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            "id",
            "name",
            "title",
        ]
        read_only_fields = [
            "id",
        ]
