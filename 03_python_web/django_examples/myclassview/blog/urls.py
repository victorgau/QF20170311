from django.conf.urls import url
from .views import PostListView, PostDetailView, create_post, create_postform, create_postmodelform

urlpatterns = [
    url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^$', PostListView.as_view(), name='post_list_view'),
    url(r'^create$', create_post, name='create_post'),
    url(r'^create1$', create_postform, name='create_postform'),
    url(r'^create2$', create_postmodelform, name='create_postmodelform'),
]
