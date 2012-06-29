# Create your views here.

from django.http import HttpResponse
from planetserve.models import Planet
import json

def index( request ):
  planetList = Planet.objects.all()
  jsonList = []
  for i in planetList:
    jsonList.append( i.toJSON() )

  return HttpResponse( json.dumps( jsonList ), content_type="application/json; charset=utf-8" )

def detail( request, planet_id ):
  return HttpResponse( json.dumps( Planet.objects.get( location__exact=planet_id ).toJSON() ), content_type="application/json; charset=utf-8" )
