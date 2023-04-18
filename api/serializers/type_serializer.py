from rest_framework import serializers

from issue_tracker.models import Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = [
            "id",
            "name",
            "title",
        ]
        read_only_fields = [
            "id",
        ]
