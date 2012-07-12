from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django import forms
from trading.passengers import calculateAvailablePassengers
from trading.mail import canCarryMail
from trading.speculative import determineGoodsAvailable

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
      
      if 'availablePassengers' not in request.session:
        availablePassengers = calculateAvailablePassengers( request.session['tradingCore'], \
                                                            request.session['passenger'] )
        request.session['availablePassengers'] = availablePassengers
        print "Calculating new available passengers: " + str( availablePassengers )
      else:
        print "Reusing available passengers from session: " + str( request.session['availablePassengers'] )
        
      return redirect( '/trading/tradingSelectPassenger' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingSelectPassenger( request ):
  if request.method == 'GET':
    t = loader.get_template( 'trading/tradingSelectPassenger.html' )
    c = RequestContext( request, {
      'high': range( request.session['availablePassengers']['high'] + 1 ),
      'middle': range( request.session['availablePassengers']['middle'] + 1 ),
      'low': range( request.session['availablePassengers']['low'] + 1),
    } )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    form = TradingSelectPassengerForm( request.POST )
    if form.is_valid():
      request.session['selectPassenger'] = form.cleaned_data
      
      # TODO validate selection vs num staterooms/steward skill
      # allocate available storage
      
      return redirect( '/trading/tradingMail' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingMail( request ):
  if request.method == 'GET':
    t = loader.get_template( 'trading/tradingMail.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    form = TradingMail( request.POST )
    if form.is_valid():
      request.session['tradingMail'] = form.cleaned_data
      
      if 'canCarryMail' not in request.session:
        mail = canCarryMail( request.session['tradingCore'], request.session['tradingMail'] )
        request.session['canCarryMail'] = mail
        print "Calculating new Can carry mail: " + str( request.session['canCarryMail'] )
      else:
        print "Reusing mail from session: " + str( request.session['canCarryMail'] )
      
      return redirect( '/trading/tradingSpeculative' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingSpeculative( request ):
  if request.method == 'GET':
    t = loader.get_template( 'trading/tradingSpeculative.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    form = TradingSpeculative( request.POST )
    if form.is_valid():
      request.session['tradingSpeculative'] = form.cleaned_data
      
      # TODO check if supplier found
      
      if 'goods' not in request.session:
        goods = determineGoodsAvailable( request.session['tradingCore'],
                                         request.session['tradingSpeculative'] )
        request.session['goods'] = goods
      
      return redirect( '/trading/tradingSelectSpeculative' )
    else:
      raise Exception( 'Form not valid', form.errors )

def tradingSelectSpeculative( request ):
  if request.method == 'GET':
    print request.session['goods']
    t = loader.get_template( 'trading/tradingSelectSpeculative.html' )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )
  elif request.method == 'POST':
    pass

def tradingSelectFreight( request ):
  if request.method == 'GET':
    pass
  elif request.method == 'POST':
    pass

def tradingNegotiateTradeGood( request ):
  if request.method == 'POST':
    return HttpResponse( '{"cost": 1000}', content_type="application/json; charset=utf-8" )
  else:
    raise Exception( 'GET not supported' )

################
# Form objects #
################
class TradingCoreForm( forms.Form ):
  startPlanet = forms.CharField( max_length=4 )
  destinationPlanet = forms.CharField( max_length = 4 )
  availableCargo = forms.IntegerField()
  numStateRooms = forms.IntegerField()
  numLowBerths = forms.IntegerField()
  addMail = forms.BooleanField( required=False )

class TradingPassengerForm( forms.Form ):
  passengerRoll = forms.IntegerField()

class TradingSelectPassengerForm( forms.Form ):
  passengerHigh = forms.IntegerField()
  passengerMiddle = forms.IntegerField()
  passengerLow = forms.IntegerField()

class TradingMail( forms.Form ):
  armed = forms.BooleanField()
  navalScoutRank = forms.IntegerField()
  socialStanding = forms.IntegerField()

class TradingSpeculative( forms.Form ):
  supplier = forms.CharField()
  search = forms.IntegerField()
  broker = forms.IntegerField()
  intOrSocial = forms.IntegerField()

# Mock page
def mock( request ):
  t = loader.get_template( 'trading/mock.html' )
  c = RequestContext( request, {} )
  return HttpResponse( t.render( c ) )
