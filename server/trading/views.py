from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django import forms
from trading.passengers import calculateAvailablePassengers

def index( request ):
  t = loader.get_template( 'trading/index.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )

def receiveInitial( request ):
  if request.method == 'POST':
    form = TradingCoreForm( request.POST )
    if form.is_valid():
      request.session['tradingCore'] = form.cleaned_data
      
      return redirect( '/trading/rollForPassengers' )
    else:
      raise Exception( 'Form not valid', form.errors )
  raise Exception( 'Method needs to be POST' )

def rollForPassengers( request ):
  t = loader.get_template( 'trading/rollForPassengers.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )

def receiveRollForPassengers( request ):
  request.session['passengerRoll'] = request.POST.get( 'passengerRoll' )
  availablePassengers = calculateAvailablePassengers( request.session['tradingCore'], \
                                                      int( request.session['passengerRoll'] ) )
  return HttpResponse( "Low " + str( availablePassengers['low'] ) + \
                       "Middle " + str( availablePassengers['middle'] ) + \
                       "High " + str( availablePassengers['high'] ) )
################
# Form objects #
################
class TradingCoreForm( forms.Form ):
  startPlanet = forms.CharField( max_length=4 )
  destinationPlanet = forms.CharField( max_length = 4 )
  availableCargo = forms.IntegerField()
  numStateRooms = forms.IntegerField()
  addMail = forms.BooleanField( required=False )

# Mock page
def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )
