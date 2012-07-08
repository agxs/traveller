from planetserve.models import Planet
from django.shortcuts import get_object_or_404
#from trading.views import TradingCore

#Agricultural +2 +1
#Asteroid -3 +1
#Barren None -5
#Desert -3 +0
#Fluid Oceans -3 +0
#Garden +2 +1
#High Population +2 -1
#Ice-Capped -3 +0
#Industrial +3 +2
#Low Population -5 +0
#Non-Agricultural -3 +1
#Non-Industrial -3 +1
#Poor -3 -3
#Rich +2 +2
#Water World -3 +0
#Amber Zone +5 -5
#Red Zone -5 No Freight

def calculateFreightTrafficModifer( startPlanetLocation, destinationPlanetLocation ):
  startPlanet = get_object_or_404( Planet, location__exact=startPlanetLocation )
  destinationPlanet = get_object_or_404( Planet, location__exact=destinationPlanetLocation )
  
  techDiff = abs( startPlanet.tech_level - destinationPlanet.tech_level )
  if ( techDiff > 5 ):
    techDiff = 5
  
  return __calculateCurrentPlanetDM( startPlanet ) + \
         __calculateDestinationPlanetDM( destinationPlanet ) - \
         techDiff

def __calculateCurrentPlanetDM( p ):
  dm = 0
  if ( p.isAgricultural() ):
    dm += 2
  if ( p.isAsteroid() ):
    dm -= 3
  if ( p.isBarren() ):
    dm += 0
  if ( p.isDesert() ):
    dm -= 3
  if ( p.isFluidOcean() ):
    dm -= 3
  if ( p.isGarden() ):
    dm += 2
  if ( p.isHighPopulation() ):
    dm += 2
  if ( p.isIceCapped() ):
    dm -= 3
  if ( p.isIndustrial() ):
    dm += 3
  if ( p.isLowPopulation() ):
    dm -= 5
  if ( p.isNonAgricultural() ):
    dm -= 3
  if ( p.isNonIndustrial() ):
    dm -= 3
  if ( p.isPoor() ):
    dm -= 3
  if ( p.isRich() ):
    dm += 2
  if ( p.isWaterWorld() ):
    dm -= 3
  if ( p.isAmberZone() ):
    dm += 5
  if ( p.isRedZone() ):
    dm -= 5
  
  return dm

def __calculateDestinationPlanetDM( p ):
  dm = 0
  if ( p.isAgricultural() ):
    dm += 1
  if ( p.isAsteroid() ):
    dm += 1
  if ( p.isBarren() ):
    dm -= 5
  if ( p.isDesert() ):
    dm += 0
  if ( p.isFluidOcean() ):
    dm += 0
  if ( p.isGarden() ):
    dm += 1
  if ( p.isHighPopulation() ):
    dm -= 1
  if ( p.isIceCapped() ):
    dm += 0
  if ( p.isIndustrial() ):
    dm += 2
  if ( p.isLowPopulation() ):
    dm += 0
  if ( p.isNonAgricultural() ):
    dm += 1
  if ( p.isNonIndustrial() ):
    dm += 1
  if ( p.isPoor() ):
    dm -= 3
  if ( p.isRich() ):
    dm += 2
  if ( p.isWaterWorld() ):
    dm += 0
  if ( p.isAmberZone() ):
    dm -= 5
  if ( p.isRedZone() ):
    raise Exception( "Can't do freight to red zone" )
  
  return dm
