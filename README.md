#В корне проекта необходимо создать файл ".env" и вписать в него переменную SECRET_KEY

------
## Запуск проекта без Docker
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
## Запуск проекта с Docker
```sh
docker-compose up
```
