from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from ..models import Post
from comments.api.serializers import CommentListSerializer
from comments.models import Comment

post_detail_url = HyperlinkedIdentityField(
    view_name='posts_api:detail',
    lookup_field='slug',
)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'title',
            'content',
            'html',
            'image',
            'timestamp',
            'publish',
            'user',
            'comments'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_html(self, obj):
        return obj.get_markdown()

    def get_comments(self, obj):

        comments_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentListSerializer(comments_qs, many=True).data
        return comments


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'title',
            'user',
            'url',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
