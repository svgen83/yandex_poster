from django.db import models

# Create your models here.
class Agency(models.Model):
    title = models.CharField('Название организации', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Подробное описание')
    latitude = models.FloatField(null=True, blank=True,
                                 verbose_name='широта')
    longitude = models.FloatField(null=True, blank=True,
                                  verbose_name='долгота')

    def __str__(self):
        return self.title


class Picture(models.Model):
    number = models.IntegerField('Номер изображения', db_index=True)
    image = models.ImageField('Изображение', db_index=True)
    agency_title = models.ForeignKey(
        Agency,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Название бюро',
        related_name='agency_titles')

    def __str__(self):
        return f'{self.number} {self.agency_title.title}'
