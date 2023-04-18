from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.project_serializer import ProjectsSerializer
from issue_tracker.models import Project


class ProjectsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all().order_by('id')
        serializer = ProjectsSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
