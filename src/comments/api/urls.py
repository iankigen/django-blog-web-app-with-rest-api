from django.conf.urls import url
from .views import (
    CommentCreateApiView,
    CommentListApiView,
    CommentDetailApiView,
)

urlpatterns = [
    url(r'^$', CommentListApiView.as_view(), name='list'),
    url(r'^create/$', CommentCreateApiView.as_view(), name='create'),
    url(r'^(?P<id>[-\w]+)/$', CommentDetailApiView.as_view(), name='detail'),
]
