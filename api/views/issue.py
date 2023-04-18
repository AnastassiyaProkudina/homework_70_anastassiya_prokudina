from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.issue_serializer import IssuesSerializer
from issue_tracker.models import Issue


class IssuesView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all().order_by('created_at')
        serializer = IssuesSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = Issue.objects.get(pk=kwargs.get("pk"))
        serializer = IssuesSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueUpdateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = Issue.objects.get(pk=kwargs.get("pk"))
        serializer = IssuesSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        obj = Issue.objects.get(pk=kwargs.get("pk"))
        serializer = IssuesSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
