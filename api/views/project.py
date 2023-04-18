from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.project_serializer import ProjectsSerializer
from issue_tracker.models import Project


class ProjectsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all().order_by('id')
        serializer = ProjectsSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = Project.objects.get(pk=kwargs.get("pk"))
        serializer = ProjectsSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = Project.objects.get(pk=kwargs.get("pk"))
        serializer = ProjectsSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        obj = Project.objects.get(pk=kwargs.get("pk"))
        serializer = ProjectsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
