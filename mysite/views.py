from django.shortcuts import render
from places.models import Agency


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
