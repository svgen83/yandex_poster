# Generated by Django 3.2.18 on 2023-07-31 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_rename_place_new_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='Номер изображения')),
                ('image', models.ImageField(db_index=True, upload_to='', verbose_name='Фотография')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sight_images', to='places.place', verbose_name='Название места')),
            ],
            options={
                'verbose_name': 'Фотография достопримечательности',
                'verbose_name_plural': 'Фотографии достопримечательности',
                'ordering': ['number'],
            },
        ),
    ]