from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('json-importer/', JsonImporter.as_view(), name='json-importer'),
    
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    
    path('profile-posts/', ProfilePostList.as_view(), name='profile-post-list'),
    path('profile-posts/<int:pk>/', ProfilePostDetail.as_view(), name='profile-post-detail'),
    
    path('posts-comments/', PostCommentList.as_view(), name='post-comment-list'),
    path('posts-comments/<int:pk>/', PostCommentDetail.as_view(), name='post-comment-detail'),
    
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    path('posts/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    path('profile-posts-and-comments/', ProfilePostsAndCommentsList.as_view(), name='profile-posts-and-comments'),
]
