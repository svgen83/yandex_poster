# Generated by Django 3.2.18 on 2023-05-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='number',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Номер изображения'),
            preserve_default=False,
        ),
    ]
