from django.shortcuts import render
from places.models import Agency
from django.urls import reverse


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
            "detailsUrl": reverse("location_urls",
                                  kwargs = {'place_id': place.id})
            }}
         )
            
   context = {"places_geojson": {
      "type":"FeatureCollection",
      "features": features}}
      
   return render(request, "index.html", context)
   
