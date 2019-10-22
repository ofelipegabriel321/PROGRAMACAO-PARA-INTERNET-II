from rest_framework import serializers
from games.models import Game
from datetime import datetime
from django.utils import timezone

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # campos que serão serialiados:
        fields = ('id',
                  'name',
                  'release_date',
                  'game_category',
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