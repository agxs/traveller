from planetserve.models import Planet
from django.shortcuts import get_object_or_404
from utils.dice import parseDiceExpr
import math

#Agricultural +0 +0
#Asteroid +1 -1
#Barren -5 -5
#Desert -1 -1
#Fluid Oceans +0 +0
#Garden +2 +2
#High Population +0 +4
#Ice-Capped +1 -1
#Industrial +2 +1
#Low Population +0 -4
#Non-Agricultural +0 +0
#Non-Industrial +0 -1
#Poor -2 -1
#Rich -1 +2
#Water World +0 +0
#Amber Zone +2 -2
#Red Zone +4 -4
#No classification +0 +0

PASSENGER_TRAFFIC_VALUE = (
  { 'low': "0", 'middle': "0", 'high': "0" }, #0 or less
  { 'low': "2d6-6", 'middle': "1d6-2", 'high': "0" }, #1
  { 'low': "2d6", 'middle': "1d6", 'high': "1d6-1d6" }, #2
  { 'low': "2d6", 'middle': "2d6-1d6", 'high': "2d6-2d6" }, #3
  { 'low': "3d6-1d6", 'middle': "2d6-1d6", 'high': "2d6-1d6" }, #4
  { 'low': "3d6-1d6", 'middle': "3d6-2d6", 'high': "2d6-1d6" }, #5
  { 'low': "3d6", 'middle': "3d6-2d6", 'high': "3d6-2d6" }, #6
  { 'low': "3d6", 'middle': "3d6-1d6", 'high': "3d6-2d6" }, #7
  { 'low': "4d6", 'middle': "3d6-1d6", 'high': "3d6-1d6" }, #8
  { 'low': "4d6", 'middle': "3d6", 'high': "3d6-1d6" }, #9
  { 'low': "5d6", 'middle': "3d6", 'high': "3d6-1d6" }, #10
  { 'low': "5d6", 'middle': "4d6", 'high': "3d6" }, #11
  { 'low': "6d6", 'middle': "4d6", 'high': "3d6" }, #12
  { 'low': "6d8", 'middle': "4d6", 'high': "4d6" }, #13
  { 'low': "7d6", 'middle': "5d6", 'high': "4d6" }, #14
  { 'low': "8d6", 'middle': "5d6", 'high': "4d6" }, #15
  { 'low': "9d6", 'middle': "6d6", 'high': "5d6" }, #16+
)

def calculateAvailablePassengers( initialForm, passengerRoll ):
  # Total passengers = start planet population + start planet traffic mod +
  #                                              end planet traffic mod +
  #                                              half Effect of player roll
  startPlanet = get_object_or_404( Planet, location__exact=initialForm['startPlanet'] )
  endPlanet = get_object_or_404( Planet, location__exact=initialForm['destinationPlanet'] )
  effect = int( math.ceil( passengerRoll / 2 ) )
  
  dm = startPlanet.population + __calculateCurrentPlanetDM( startPlanet ) + \
                                __calculateDestinationPlanetDM( endPlanet ) + \
                                effect
  if ( dm < 0 ):
    dm = 0;
  if ( dm > 16 ):
    dm = 16
  
  p = PASSENGER_TRAFFIC_VALUE[dm]
  low = parseDiceExpr( p['low'] )
  middle = parseDiceExpr( p['middle'] )
  high = parseDiceExpr( p['high'] )
  if ( low < 0 ):
    low = 0
  if ( middle < 0 ):
    middle = 0;
  if ( high < 0 ):
    high = 0;
  return { 'low': low, 'middle': middle, 'high': high }

def __calculateCurrentPlanetDM( p ):
  dm = 0
  if ( p.isAsteroid() ):
    dm += 1
  if ( p.isBarren() ):
    dm -= 5
  if ( p.isDesert() ):
    dm -= 1
  if ( p.isGarden() ):
    dm += 2
  if ( p.isIceCapped() ):
    dm += 1
  if ( p.isIndustrial() ):
    dm += 2
  if ( p.isPoor() ):
    dm -= 2
  if ( p.isRich() ):
    dm -= 1
  if ( p.isAmberZone() ):
    dm += 2
  if ( p.isRedZone() ):
    dm += 4
  
  return dm

def __calculateDestinationPlanetDM( p ):
  dm = 0
  if ( p.isAsteroid() ):
    dm -= 1
  if ( p.isBarren() ):
    dm -= 5
  if ( p.isDesert() ):
    dm -= 1
  if ( p.isGarden() ):
    dm += 2
  if ( p.isHighPopulation() ):
    dm += 4
  if ( p.isIceCapped() ):
    dm -= 1
  if ( p.isIndustrial() ):
    dm += 1
  if ( p.isLowPopulation() ):
    dm -= 4
  if ( p.isNonIndustrial() ):
    dm -= 1
  if ( p.isPoor() ):
    dm -= 1
  if ( p.isRich() ):
    dm += 2
  if ( p.isAmberZone() ):
    dm -= 2
  if ( p.isRedZone() ):
    dm -= 4
  
  return dm
