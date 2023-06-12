from django.shortcuts import get_object_or_404
from places.models import Agency
from django.http import HttpResponse, JsonResponse


def show_location(request, place_id):
   
    location = get_object_or_404(Agency, pk=place_id)
    
    data = {
       "title": location.title,
       "description_short": location.description_short,
       "description_long": location.description_long,
       "coordinates": {
          "lat": location.latitude,
          "lon": location.longitude},
       "images": []}
    
    for title in location.agency_titles.all():
        data["images"].append(title.image.url)        

    return JsonResponse(data, json_dumps_params={
            'ensure_ascii': False,
            'indent': 2})
