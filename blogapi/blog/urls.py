from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EndpointsList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('json-importer/', JsonImporter.as_view()),
    
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),
    
    path('profile-posts/', ProfilePostList.as_view()),
    path('profile-posts/<int:pk>/', ProfilePostDetail.as_view()),
    
    path('posts-comments/', PostCommentList.as_view()),
    path('posts-comments/<int:pk>/', PostCommentDetail.as_view()),
    
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),

    path('posts/<int:pk>/comments/', CommentList.as_view()),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentDetail.as_view()),
    
    path('profile-posts-and-comments/', ProfilePostsAndCommentsList.as_view()),
]