from django.shortcuts import render, get_object_or_404
from places.models import Agency
from django.http import HttpResponse, JsonResponse


def index(request):
   places = Agency.objects.all()
   agency_places = []
   for place in places:
      agency_places.append(
         {"type": "Feature",
         "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]},
          "properties": {
            "title": place.title,
            "placeId": place.pk,
            #"detailsUrl": "./places/moscow_legends.json"
            }}
         )
   data = {"places_geojson": {
      "type": "FeatureCollection",
      "features": agency_places}}
   return render(request, "index.html", context=data)


def show_location(request, place_id):
   
    location = get_object_or_404(Agency, pk=place_id)

    response = JsonResponse(
       {
       "title": location.title,
       "description_short": location.description_short,
       "description_long": location.description_long,
       "coordinates": {
          "lat": location.latitude,
          "lon": location.longitude
          }},
       json_dumps_params={'ensure_ascii': False})

    return response
