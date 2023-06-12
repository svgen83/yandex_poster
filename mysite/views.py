from django.shortcuts import render, get_object_or_404
from places.models import Agency
from django.http import HttpResponse, JsonResponse


def index(request):
   places = Agency.objects.all()
   features = []
   
   for place in places:
      features.append(
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
            
   context = {"places_geojson": {"type":"FeatureCollection",
                       "features": features}}
      
   return render(request, "index.html", context)
   
