from django.template import Context, loader
from django.http import HttpResponse

def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = Context( {} )
  return HttpResponse( t.render( c ) )
