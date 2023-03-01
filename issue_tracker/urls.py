from django.urls import path

from issue_tracker.views.base import IndexView, IndexRedirectView
from issue_tracker.views.issues import IssueCreateView, IssueDetail, IssueUpdateView, IssueDeleteView, \
    IssueConfirmDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("issue/", IndexRedirectView.as_view(), name='issues_index_redirect'),
    path("issue/create", IssueCreateView.as_view(), name="issue_create"),
    path("issue/<int:pk>", IssueDetail.as_view(), name="issue_detail"),
    path("issue/<int:pk>/update/", IssueUpdateView.as_view(), name="issue_update"),
    path("issue/<int:pk>/delete/", IssueDeleteView.as_view(), name="issue_delete"),
    path("issue/<int:pk>/confirm_delete/", IssueConfirmDeleteView.as_view(), name="issue_confirm_delete"),
]
