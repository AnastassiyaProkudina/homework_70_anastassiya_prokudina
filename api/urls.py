from django.urls import path

from api.views.project import ProjectsAPIView

urlpatterns = [
    path("projects/", ProjectsAPIView.as_view(), name="projects"),
]
