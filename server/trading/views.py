from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from trading.passengers import calculateAvailablePassengers

def index( request ):
  t = loader.get_template( 'trading/index.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )

def receiveInitial( request ):
  request.session['startPlanet'] = request.POST.get( 'startPlanet' )
  request.session['destinationPlanet'] = request.POST.get( 'destinationPlanet' )
  
  # Store the entered cargo space, and also keep track of a running total
  request.session['availableCargo'] = request.POST.get( 'availableCargo' )
  request.session['initialCargo'] = request.POST.get( 'availableCargo' )
  
  # Same with the number of available state rooms
  request.session['numStateRooms'] = request.POST.get( 'numStateRooms' )
  request.session['initialStateRooms'] = request.POST.get( 'numStateRooms' )
  
  request.session['addMail'] = request.POST.get( 'addMail' )
  
  return redirect( '/trading/rollForPassengers' )

def rollForPassengers( request ):
  t = loader.get_template( 'trading/rollForPassengers.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )

def receiveRollForPassengers( request ):
  request.session['passengerRoll'] = request.POST.get( 'passengerRoll' )
  availablePassengers = calculateAvailablePassengers( request )
  return HttpResponse( "Low " + str( availablePassengers['low'] ) + \
                       "Middle " + str( availablePassengers['middle'] ) + \
                       "High " + str( availablePassengers['high'] ) )

def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )
