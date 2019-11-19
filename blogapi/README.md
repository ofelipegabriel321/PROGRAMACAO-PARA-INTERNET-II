# Blog API

## Executando o projeto
Instale os requerimentos do projeto com o comando:
```
$ pip install -r requirements.txt
```

Após isso execute o makemigrations e o migrate:
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```

Agora você pode rodar o servidor a partir de:
```
$ python manage.py runserver
```

Para povoar o banco de dados, execute, no servidor, o POST na url do 'json-importer' (se você está num servidor local, basta ir no link localhost:8000/json-importer/). Após isso você pode testar a API povoada.


## Apresentação do projeto

>> https://youtu.be/p-6MOf1qEJ0
