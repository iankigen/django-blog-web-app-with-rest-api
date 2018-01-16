from django.conf.urls import url
from .views import (
    CommentListApiView,
    CommentDetailApiView,
)

urlpatterns = [
    url(r'^$', CommentListApiView.as_view(), name='list'),
    url(r'^(?P<id>[-\w]+)/$', CommentDetailApiView.as_view(), name='detail'),
]
