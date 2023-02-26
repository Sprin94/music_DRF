from datetime import date

from django.core.exceptions import ValidationError

from django.db import models


def validator_year(value):
    if date.today().year < value:
        raise ValidationError('Год не может быть больше текущего')


class Singer(models.Model):
    """Исполнитель."""
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    """Альбом"""
    singer = models.ForeignKey(
        verbose_name='Исполнитель',
        to=Singer,
        on_delete=models.CASCADE,
        related_name='albums'
    )
    release_year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[validator_year]
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.singer.name}: {self.release_year}г.'


class Song(models.Model):
    """Песня"""
    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    albums = models.ManyToManyField(
        verbose_name='Номер в альбоме',
        to=Album,
        blank=True,
    )

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.name
