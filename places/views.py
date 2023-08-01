from django.shortcuts import get_object_or_404
from places.models import Place
from django.http import JsonResponse


def show_location(request, place_id):

    locations = get_object_or_404(Place, pk=place_id)

    place_description = {
       "title": locations.title,
       "description_short": locations.description_short,
       "description_long": locations.description_long,
       "coordinates": {
          "lat": locations.latitude,
          "lon": locations.longitude},
       "imgs": [title.image.url for title in locations.place_images.all()]}

    return JsonResponse(place_description,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2})
