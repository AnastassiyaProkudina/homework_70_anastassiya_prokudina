from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.issue_serializer import IssuesBaseSerializer
from issue_tracker.models import Issue


class IssuesView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all().order_by('created_at')
        serializer = IssuesBaseSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)