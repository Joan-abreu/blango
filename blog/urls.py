from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, AuthorProfileDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('author-profile/<int:pk>/', AuthorProfileDetailView.as_view(), name='author-profile-detail'),
]
