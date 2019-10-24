from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import AccountSerializer

@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        # faz uma lista com todos os Account
        accounts = Account.objects.all()
        # faz a serialização (Model -> JSON)
        # o many=True serve para serializar uma lista de objetos
        # em vez de uma única instância de objeto
        accounts_serializer = AccountSerializer(accounts, many=True)
        return Response(accounts_serializer.data)
    
    elif request.method == 'POST':
        # faz a deserialização (JSON -> Model) passando os dados necessários
        account_serializer = AccountSerializer(data=request.data)
        # salva o account caso seja válido, depois
        # retorna account_serializer.data e 201
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        
        # account inválido retorna 400
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, id):
    # tenta pegar o account esse determinado id
    try:
        account = Account.objects.get(id=id)
    # sem achar accounts com o id, retorna 404
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # faz a serialização (Model -> JSON)
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)
        
    elif request.method == 'PUT':
        # faz a deserialização (JSON -> Model) passando os dados necessários
        account_serializer = AccountSerializer(account, data=request.data)
        # salva o account caso seja válido, depois retorna
        # game_serializer.data
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data)
        
        # account inválido retorna 400
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # exclui o account e retorna 204
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)