from trading.freight import calculateFreightTrafficModifer
from django.shortcuts import get_object_or_404
from planetserve.models import Planet
from utils.dice import parseDiceExpr
import logging

logger = logging.getLogger( __name__ )

def canCarryMail( tradingCore, tradingMail ):
  tm = calculateFreightTrafficModifer( tradingCore['startPlanet'], tradingCore['destinationPlanet'] )
  
  mailMod = 0
  if tm <= -10:
    mailMod -= 2
  elif tm <= -5:
    mailMod -= 1
  elif tm <= 4:
    mailMod += 0
  elif tm <= 9:
    mailMod += 1
  elif tm >= 10:
    mailMod += 2
  else:
    raise Exception( 'Whoa mail broken - wtf is tm? ', tm )
  
  if tradingMail['armed']:
    mailMod += 2
  
  mailMod += tradingMail['navalScoutRank']
  mailMod += tradingMail['socialStanding']
  
  startPlanet = get_object_or_404( Planet, location__exact=tradingCore['startPlanet'] )
  
  if startPlanet.tech_level <= 5:
    mailMod -= 4
  
  mailRoll = parseDiceExpr( "2d12+" + str( mailMod ) )
  logger.info( "Rolled " + str( mailRoll ) + " for mail." )
  return mailRoll >= 12
