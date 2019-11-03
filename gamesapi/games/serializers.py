from rest_framework import serializers
from games.models import *
from datetime import datetime
from django.utils import timezone

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    # o SlugRelatedField recebe no queryset todos os objetos da classe que
    # está sendo acessada e no slug_field, em forma de string, qual é o campo
    # acessado dentro da classe
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                                                 slug_field='name')
    class Meta:
        model = Game
        # campos que serão serialiados:
        fields = ('url',
                  'game_category',
                  'id',
                  'name',
                  'release_date',
                  'played')

    @staticmethod
    def validate_name(value):
        games = Game.objects.filter(name=value)
        if games:
            raise serializers.ValidationError("Não podem haver dois jogos com o mesmo nome.")
        return value
    
    @staticmethod
    def validate_delete(game):
        if game.release_date <= timezone.make_aware(datetime.now(), timezone.get_current_timezone()):
            raise serializers.ValidationError("Um jogo já lançado não pode ser excluído.")
        return game

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
    # Como cada jogador deve ter uma lista de escores, devemos fazer
    # um campo scores com os escores como ScoreSerializer.
    # O read_only serve para determinar que as alterações em scores
    # não afete diretamente os escores
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url',
                  'name',
                  'gender',
                  'scores')
