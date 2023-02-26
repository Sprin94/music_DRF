В корне проекта необходимо создать файл ".env" и вписать в него переменную SECRET_KEY

------
## Запусе проекта без Docker
Устанавливаем зависимости:
```sh
pip install -r ./requirements.txt
```

Создаем миграции:
```sh
python manage.py makemigrations
```

Применяем миграции:
```sh
python manage.py migrate
```

Запускаем локальный сервер:
```sh
python manage.py runserver localhost:8000
```
## Запусе проекта с Docker
Устанавливаем зависимости:
```sh
docker-compose up
```
