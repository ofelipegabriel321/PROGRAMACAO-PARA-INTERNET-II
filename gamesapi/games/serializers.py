from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # campos que serão serialiados:
        fields = ('id',
                  'name',
                  'release_date',
                  'game_category',
                  'played')