from django.urls import path

from api.views.issue import IssueDetailAPIView, IssuesView
from api.views.project import ProjectsAPIView, ProjectDetailAPIView

urlpatterns = [
    path("projects/", ProjectsAPIView.as_view(), name="projects"),
    path("issues/", IssuesView.as_view(), name="issues"),
    path("project/<int:pk>", ProjectDetailAPIView.as_view(), name="api_project_detail_"),
    path("issue/<int:pk>", IssueDetailAPIView.as_view(), name="api_issue_detail_"),
]
