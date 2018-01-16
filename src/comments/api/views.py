from rest_framework.filters import (
    SearchFilter
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .serializers import (
    CommentListSerializer,
    CommentDeleteSerializer,
    CommentDetailSerializer
)
from ..models import Comment

from posts.api.pagination import PostPageNumberPagination
from posts.api.permissions import IsOwnerOrReadOnly


#
# class CommentCreateApiView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentsSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#
class CommentDeleteApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentDetailApiView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    lookup_url_kwarg = 'id'


class CommentListApiView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['content', 'user__first_name', 'user__last_name']
    pagination_class = PostPageNumberPagination
