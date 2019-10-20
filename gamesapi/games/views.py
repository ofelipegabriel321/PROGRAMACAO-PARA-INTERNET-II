from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer

@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        # faz uma lista com todos os Games
        games = Game.objects.all()
        # faz a serialização (Model -> JSON)
        # o many=True serve para serializar uma lista de objetos
        # em vez de uma única instância de objeto
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    
    elif request.method == 'POST':
        # faz a deserialização (JSON -> Model) passando os dados necessários
        game_serializer = GameSerializer(data=request.data)
        # salva o jogo caso seja válido, depois
        # retorna game_serializer.data e 201
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
        
        # jogo inválido retorna 400
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST'])
def game_detail(request, id):
    # tenta pegar o jogo esse determinado id
    try:
        game = Game.objects.get(id=id)
    # sem achar jogos com o id, retorna 404
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # faz a serialização (Model -> JSON)
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)
        
    elif request.method == 'PUT':
        # faz a deserialização (JSON -> Model) passando os dados necessários
        game_serializer = GameSerializer(game, data=request.data)
        # salva o jogo caso seja válido, depois retorna
        # game_serializer.data
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data)
        
        # jogo inválido retorna 400
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # exclui o jogo e retorna 204
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)