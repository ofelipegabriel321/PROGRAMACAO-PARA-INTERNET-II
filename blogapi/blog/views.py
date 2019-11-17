from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from .permissions import *

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
        permissions.IsAdminUser,
    )
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ProfileList(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        profile_serializer = ProfileSerializer(profiles, many=True)
        return Response(profile_serializer.data)

    def post(self, request, format=None):
        profile = request.data
        profile_serializer = ProfileSerializer(data=profile)
        
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyProfile,
    )
    
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile_serializer = ProfileSerializer(profile)
        return Response(profile_serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile_serializer = ProfileSerializer(profile, data=request.data)
        
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data)
        
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile_serializer = ProfileSerializer(data=request.data)
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_200_OK)


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
    name = 'profile-detail'


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
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)

    def put(self, request, pk, format=None):
        request.data['userId'] = request.user.pk
        post = self.get_object(pk)
        post_serializer = PostSerializer(post, data=request.data)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post_serializer = ProfileSerializer(data=request.data)
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)


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
        return Response(comment_serializer.data)
    
    def post(self, request, pk, format=None):
        request.data['postId'] = pk
        comment = request.data
        comment_serializer = CommentSerializer(data=comment)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnlyComment,
    )
    
    serializer_class = CommentSerializer
    name = 'comment-detail'
    lookup_url_kwarg = 'comment_pk'

    def get_queryset(self):
        post_pk = self.kwargs['post_pk']
        return Comment.objects.filter(postId=post_pk)

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

class EndpointsList(APIView):

    def get(self, request, format=None):
        root_url = 'http://localhost:8000/'
        data = {
                'json-importer': root_url + 'json-importer/',
                'profiles-list': root_url + 'profiles/',
                'profile-posts-list': root_url + 'profile-posts/',
                'posts-list': root_url + 'posts/',
                'posts-comments-list': root_url + 'posts-comments/',
                'profile-posts-and-comments-list': root_url + 'profile-posts-and-comments/',
                'user-list': root_url + 'users'
        }
        
        return Response(data)
