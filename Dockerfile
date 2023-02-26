FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . ./usr/src/code

WORKDIR /usr/src/code

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py collectstatic --noinput \
    && python manage.py migrate --noinput \
    && gunicorn settings.wsgi:application --bind 0.0.0.0:8000
