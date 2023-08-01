import logging
import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Picture


def download_image_content(index, img_url):
    response = requests.get(img_url)
    response.raise_for_status()
    return {'content': response.content,
            'image_name': img_url.split('/')[-1],
            'image_number': index}


def upload_image(image_content, place_title):
    upload_content = ContentFile(
        image_content['content'],
        name=image_content['image_name'])
    Picture.objects.create(
        image=upload_content,
        sight=place_title,
        number=image_content['image_number'])


class Command(BaseCommand):
    help = 'Команда для загрузки данных в базу из файла json'

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_description = response.json()
        place_title, created = Place.objects.get_or_create(
            title=place_description['title'],
            latitude=place_description['coordinates']['lat'],
            longitude=place_description['coordinates']['lng'],
            defaults={
                'description_short': place_description['description_short'],
                'description_long': place_description['description_long']})
        if created:
            logging.warning(
                f'Создан новый объект "{place_description["title"]}"')
            for index, img_url in enumerate(place_description['imgs']):
                image_content = download_image_content(index, img_url)
                upload_image(image_content, place_title)
            logging.warning('Картинки загружены')

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='json url')
