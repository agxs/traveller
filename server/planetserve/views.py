# Create your views here.

from django.http import HttpResponse
from planetserve.models import Planet
import json

def index( request ):
  return HttpResponse( json.dumps( Planet.objects.all() ) )

def detail( request, planet_id ):
  return HttpResponse( json.dumps( Planet.objects.get( location__exact=planet_id ).toJSON() ) )
