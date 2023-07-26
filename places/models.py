from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Place(models.Model):
    title = models.CharField('Название организации', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Подробное описание')
    latitude = models.FloatField(null=True, blank=True,
                                 verbose_name='широта')
    longitude = models.FloatField(null=True, blank=True,
                                  verbose_name='долгота')
    class Meta:
        verbose_name = 'Агенство по туризму'
        verbose_name_plural = 'Агенства по туризму'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Picture(models.Model):
    number = models.IntegerField('Номер изображения',
                                 db_index=True, default=0)
    image = models.ImageField(verbose_name='Фотография',
                              db_index=True)
    place_title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Название бюро',
        related_name='place_images')
        
    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательности'
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place_title.title}'
