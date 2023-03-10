from django.urls import path

from issue_tracker.views.base import IndexView, IndexRedirectView
from issue_tracker.views.issues import IssueCreateView, IssueDetail, IssueUpdateView, IssueDeleteView, \
    IssueConfirmDeleteView
from issue_tracker.views.projects import ProjectListView, ProjectDetail, ProjectUpdateView, ProjectCreateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("issue/", IndexRedirectView.as_view(), name='issues_index_redirect'),
    path("issue/create", IssueCreateView.as_view(), name="issue_create"),
    path("issue/<int:pk>", IssueDetail.as_view(), name="issue_detail"),
    path("issue/<int:pk>/update/", IssueUpdateView.as_view(), name="issue_update"),
    path("issue/<int:pk>/delete/", IssueDeleteView.as_view(), name="issue_delete"),
    path("issue/<int:pk>/confirm_delete/", IssueConfirmDeleteView.as_view(), name="issue_confirm_delete"),
    path("project/", ProjectListView.as_view(), name='project_list'),
    path("project/create", ProjectCreateView.as_view(), name="project_create"),
    path("project/<int:pk>", ProjectDetail.as_view(), name="project_detail"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
]
