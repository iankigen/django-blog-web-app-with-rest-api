from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/posts/', include('posts.api.urls', namespace='posts_api')),
    url(r'^api/comments/', include('comments.api.urls', namespace='comments_api')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
