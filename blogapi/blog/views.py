from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from django.http import Http404
from .serializers import *
from .models import *
from .permissions import *


class ApiRoot(APIView):

    def get(self, request, *args, **kwargs):

        data = {
            'api-token-auth': reverse('api-token-auth', request=request),
            'json-importer': reverse('json-importer', request=request),
            'users': reverse('user-list', request=request),
            'profiles': reverse('profile-list', request=request),
            'profiles-posts': reverse('profile-post-list', request=request),
            'posts-comments': reverse('post-comment-list', request=request),
            'posts': reverse('post-list', request=request),
            'profile-posts-and-comments': reverse('profile-posts-and-comments', request=request)
        }

        return Response(data, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    throttle_scope = 'api-token'
    throttle_classes = (
        ScopedRateThrottle,
    )
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name': user.username
        })


class JsonImporter(APIView):
    
    def post(self, request, format=None):
        posts = request.data['posts']
        comments = request.data['comments']
        profiles = request.data['users']

        for profile in profiles:
            user_serializer = UserSerializer(data=profile)
            if user_serializer.is_valid():
                user_serializer.save()
            profile_serializer = ProfileSerializer(data=profile)
            if profile_serializer.is_valid():
                profile_serializer.save()

        for post in posts:
            post_serializer = PostSerializer(data=post)
            if post_serializer.is_valid():
                post_serializer.save()

        for comment in comments:
            comment_serializer = CommentSerializer(data=comment)
            if comment_serializer.is_valid():
                comment_serializer.save()
        
        return Response(status=status.HTTP_200_OK)


class UserList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ProfileList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyProfile,
    )
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class ProfilePostList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'


class ProfilePostDetail(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyProfile,
    )

    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'


class PostCommentList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'


class PostCommentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyPost,
    )

    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-detail'


class PostList(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get(self, request, format=None):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)
    
    def post(self, request, format=None):
        request.data['userId'] = request.user.pk
        post = request.data
        post_serializer = PostSerializer(data=post)

        self.check_object_permissions(self.request, post_serializer)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyPost,
    )
    
    def get_object(self, pk):
        try:
            obj = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        request.data['userId'] = request.user.pk
        post = self.get_object(pk)
        post_serializer = PostSerializer(post, data=request.data)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_object(self, pk):
        try:
            return Comment.objects.filter(postId=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comments = self.get_object(pk)
        comment_serializer = CommentSerializer(comments, many=True)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        request.data['postId'] = pk
        request.data['email'] = request.user.email
        comment = request.data
        comment_serializer = CommentSerializer(data=comment)

        self.check_object_permissions(self.request, comment_serializer)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyComment,
    )
    
    def get_object(self, post_pk, comment_pk):
        try:
            comments = Comment.objects.filter(postId=post_pk)
            try:
                obj = comments.get(pk=comment_pk)
                self.check_object_permissions(self.request, obj)
                return obj
            except Comment.DoesNotExist:
                raise Http404
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfilePostsAndCommentsList(APIView):

    def get(self, request, format=None):
        response = []
        profiles = Profile.objects.all()
        for profile in profiles:
            profile_data = {}
            
            profile_data['id'] = profile.id
            profile_data['name'] = profile.name

            count_posts = 0
            count_comments = 0

            for post in profile.posts.all():
                count_posts += 1
                for comment in post.comments.all():
                    count_comments += 1

            profile_data['total_posts'] = count_posts
            profile_data['total_comments'] = count_comments

            response.append(profile_data)

        return Response(response)
