from django.urls import path

from issue_tracker.views.base import IndexView, IndexRedirectView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("issue/", IndexRedirectView.as_view(), name='issues_index_redirect'),
]
