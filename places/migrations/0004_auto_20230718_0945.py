# Generated by Django 3.2.18 on 2023-07-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_picture_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ['pk'], 'verbose_name': 'Агенство по туризму', 'verbose_name_plural': 'Агенства по туризму'},
        ),
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['number'], 'verbose_name': 'Фотография достопримечательности', 'verbose_name_plural': 'Фотографии достопримечательности'},
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(db_index=True, upload_to='', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='number',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Номер изображения'),
        ),
    ]
