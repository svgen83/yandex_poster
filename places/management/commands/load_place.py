import logging
import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Picture


def get_or_create_content(place_description):
    place, created = Place.objects.get_or_create(
        title=place_description['title'],
        description_short=place_description['description_short'],
        description_long=place_description['description_long'],
        latitude=place_description['coordinates']['lat'],
        longitude=place_description['coordinates']['lng'])
    logging.warning(f'Создан новый объект "{place_description["title"]}"')
    return place, created


def get_place_description(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_images(img_urls, place):
    for index, img_url in enumerate(img_urls):
        image_name = img_url.split('/')[-1]
        response = requests.get(img_url)
        response.raise_for_status()
        image_content = ContentFile(response.content, name=image_name)
        Picture.objects.create(
            image=image_content,
            sight=place,
            number=index)
    logging.warning('Картинки загружены')


class Command(BaseCommand):
    help = 'Команда для загрузки данных в базу из файла json'

    def handle(self, *args, **options):
        url = options['url']
        place_description = get_place_description(url)
        place, created = get_or_create_content(place_description)
        if created:
            get_images(place_description['imgs'], place)

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='json url')
