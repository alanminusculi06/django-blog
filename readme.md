# Django Blog

O Django Blog é uma exemplo de blog básico desenvolvido a partir do tutorial [Django Girls](https://tutorial.djangogirls.org/pt/)

## Linguagem/Tecnologias
- Python 3.8
- Django
- Pillow (upload de imagens)
- Docker

## Executar
- Instale o [Docker](https://docs.docker.com/engine/install/)
- Clone o repositório
```
git clone https://github.com/alanminusculi06/django-blog
```
- Acesse o diretório django-blog
```
cd django-blog
```
- Execute o docker-compose
```
docker-compose up -d --build
```
- Crie o super usuário
```
docker exec -it app python manage.py createsuperuser
```
- Acesse [http://localhost:8000/admin](http://localhost:8000/admin)
