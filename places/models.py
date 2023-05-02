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
