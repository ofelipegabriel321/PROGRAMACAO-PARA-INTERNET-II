from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='profile')


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
