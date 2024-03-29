# Generated by Django 3.2.18 on 2023-07-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_rename_agency_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['pk'], 'verbose_name': 'Интересное место', 'verbose_name_plural': 'Интересные места'},
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название места'),
        ),
    ]
