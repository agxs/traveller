from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django import forms
from trading.passengers import calculateAvailablePassengers

def tradingCore( request ):
  if request.method == 'GET':
    t = loader.get_template( 'trading/tradingCore.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    form = TradingCoreForm( request.POST )
    if form.is_valid():
      request.session['tradingCore'] = form.cleaned_data
      
      return redirect( '/trading/tradingPassenger' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingPassenger( request ):
  if request.method == 'GET':
    t = loader.get_template( 'trading/tradingPassenger.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    form = TradingPassengerForm( request.POST )
    if form.is_valid():
      request.session['passenger'] = form.cleaned_data
      
      return redirect( '/trading/tradingSelectPassenger' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingSelectPassenger( request ):
  if request.method == 'GET':
    if 'availablePassengers' not in request.session:
      availablePassengers = calculateAvailablePassengers( request.session['tradingCore'], \
                                                          request.session['passenger'] )
      request.session['availablePassengers'] = availablePassengers
      print "Calculating new available passengers: " + str( availablePassengers )
    else:
      print "Reusing available passengers from session: " + str( request.session['availablePassengers'] )
    t = loader.get_template( 'trading/tradingSelectPassenger.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    pass

def tradingMail( request ):
  if request.method == 'GET':
    pass
  elif request.method == 'POST':
    pass

def tradingSpeculative( request ):
  if request.method == 'GET':
    pass
  elif request.method == 'POST':
    pass

def tradingSelectSpeculative( request ):
  if request.method == 'GET':
    pass
  elif request.method == 'POST':
    pass

def tradingSelectFreight( request ):
  if request.method == 'GET':
    pass
  elif request.method == 'POST':
    pass

################
# Form objects #
################
class TradingCoreForm( forms.Form ):
  startPlanet = forms.CharField( max_length=4 )
  destinationPlanet = forms.CharField( max_length = 4 )
  availableCargo = forms.IntegerField()
  numStateRooms = forms.IntegerField()
  addMail = forms.BooleanField( required=False )

class TradingPassengerForm( forms.Form ):
  passengerRoll = forms.IntegerField()

# Mock page
def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )
