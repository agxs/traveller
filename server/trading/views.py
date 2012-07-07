from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from utils.dice import d6

def index( request ):
  t = loader.get_template( 'trading/index.html' )
  c = Context( {} )
  return HttpResponse( t.render( c ) )

def receiveInitial( request ):
  request.session['startPlanet'] = request.POST.get( 'startPlanet' )
  request.session['destinationPlanet'] = request.POST.get( 'destinationPlanet' )
  request.session['availableCargo'] = request.POST.get( 'availableCargo' )
  request.session['numStateRooms'] = request.POST.get( 'numStateRooms' )
  request.session['addMail'] = request.POST.get( 'addMail' )
  
  return redirect( '/trading/rollForPassengers' )

def rollForPassengers( request ):
  t = loader.get_template( 'trading/rollForPassengers.html' )
  c = Context( {} )
  return HttpResponse( t.render( c ) )

def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = Context( {} )
  return HttpResponse( t.render( c ) )
