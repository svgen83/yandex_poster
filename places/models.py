from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    latitude = models.FloatField(verbose_name='широта')
    longitude = models.FloatField(verbose_name='долгота')

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Picture(models.Model):
    number = models.IntegerField('Номер изображения',
                                 db_index=True,
                                 blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография',
                              db_index=True)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Достопримечательность',
        related_name='images')

    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательности'
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place.title}'
