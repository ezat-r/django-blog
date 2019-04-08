from django.conf.urls import url
from .views import getPosts, postDetail, createOrEditPost

urlpatterns = [
    url(r"^$", getPosts, name="get_posts"),
    url("^(?P<pk>\d+)/$", postDetail, name="post_detail"),
    url(r"^new/$", createOrEditPost, name="new_post"),
    url(r"^(?P<pk>\d+)/edit/$", createOrEditPost, name="edit_post"),
]