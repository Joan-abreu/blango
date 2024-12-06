from django.urls import path
from blog.views import index, post_detail

urlpatterns = [
    path("", index, name="index"),
		path("post/<slug>/", post_detail, name="blog-post-detail")
]