from django.shortcuts import get_object_or_404
from places.models import Place
from django.http import JsonResponse


def show_location(request, place_id):
   
    location = get_object_or_404(Place, pk=place_id)
    
    data = {
       "title": location.title,
       "description_short": location.description_short,
       "description_long": location.description_long,
       "coordinates": {
          "lat": location.latitude,
          "lon": location.longitude},
       "imgs": []}
    
    for title in location.place_images.all():
        data["imgs"].append(title.image.url)        

    return JsonResponse(data, json_dumps_params={
            'ensure_ascii': False,
            'indent': 2})
