from django.urls import path
from blog.views import AllPosts, NewPost, single_blog

urlpatterns = [
    path("", AllPosts.as_view(), name="blogs_page"),
    path("<int:pk>/", single_blog, name="single_blog"),
    path("create/", NewPost.as_view(), name="create_post_page")
]
