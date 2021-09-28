from django.urls import path
from blog.views import AllPosts, NewPost

urlpatterns = [
    path("", AllPosts.as_view(), name="blogs_page"),
    path("create/", NewPost.as_view(), name="create_post_page")
]
