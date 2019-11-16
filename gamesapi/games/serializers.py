from rest_framework import serializers
from games.models import *
from datetime import datetime
from django.utils import timezone

class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url','name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'pk','username','games')

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url',
                  'pk',
                  'name',
                  'games')

class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                                                 slug_field='name')
    class Meta:
        model = Game
        fields = ('url',
                  'owner',
                  'pk',
                  'game_category',
                  'name',
                  'release_date',
                  'played')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(),
                                        slug_field='name')

    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                          slug_field='name')
    
    class Meta:
        model = Score
        fields = ('url',
                  'pk',
                  'score',
                  'score_date',
                  'player',
                  'game')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url',
                  'name',
                  'gender',
                  'scores')
