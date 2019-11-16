from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['pk', 'street', 'suite', 'city', 'zipcode']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email']
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'],
                                   password='password12345')
        return user

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ['pk', 'name', 'email', 'address']

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.get(email=validated_data['email'])
        address_data = validated_data['address']
        validated_data['address'] = Address.objects.create(**address_data)
        profile = Profile.objects.create(user=user,
                                         **validated_data)
        return profile

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        address.street = address_data.get('street', address.street)
        address.suite = address_data.get('suite', address.suite)
        address.city = address_data.get('city', address.city)
        address.zipcode = address_data.get('zipcode', address.zipcode)
        instance.save()
        address.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'userId', 'title', 'body']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'postId', 'name', 'email', 'body']


class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['pk', 'name', 'email', 'posts']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = ['pk', 'userId', 'title', 'body', 'comments']
