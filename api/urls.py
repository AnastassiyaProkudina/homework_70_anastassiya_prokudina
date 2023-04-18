from django.urls import path

from api.views.issue import IssueDetailAPIView, IssuesView, IssueUpdateAPIView, IssueDeleteAPIView
from api.views.project import ProjectsAPIView, ProjectDetailAPIView, ProjectUpdateAPIView, ProjectDeleteAPIView

urlpatterns = [
    path("projects/", ProjectsAPIView.as_view(), name="projects"),
    path("project/<int:pk>", ProjectDetailAPIView.as_view(), name="api_project_detail"),
    path("project/<int:pk>/update/", ProjectUpdateAPIView.as_view(), name="api_project_update"),
    path("project/<int:pk>/delete/", ProjectDeleteAPIView.as_view(), name="api_project_delete"),
    path("issues/", IssuesView.as_view(), name="issues"),
    path("issue/<int:pk>", IssueDetailAPIView.as_view(), name="api_issue_detail_"),
    path("issue/<int:pk>/update/", IssueUpdateAPIView.as_view(), name="api_issue_update"),
    path("issue/<int:pk>/delete/", IssueDeleteAPIView.as_view(), name="api_issue_delete"),
]
