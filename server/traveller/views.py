# Create your views here.

from django.http import HttpResponse

def home( request ):
  return HttpResponse( "This is a test traveller app. Try going to /planets/." )

