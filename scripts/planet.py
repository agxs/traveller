#!/usr/bin/env python

import sys
import traceback
import random

size = {
  0: '800 km',
  1: '1600 km',
  2: '3200 km',
  3: '4800 km',
  4: '6400 km',
  5: '8000 km',
  6: '9600 km',
  7: '11200 km',
  8: '12800 km',
  9: '14400 km',
  10: '16000 km'
}

atmosphere = {
  0: 'None',
  1: 'Trace',
  2: 'Very Thin, Tainted',
  3: 'Very Thin',
  4: 'Thin, Tainted',
  5: 'Thin',
  6: 'Standard',
  7: 'Standard, Tainted',
  8: 'Dense',
  9: 'Dense, Tainted',
  10: 'Exotic',
  11: 'Corrosive',
  12: 'Insidious',
  13: 'Dense, High',
  14: 'Thin, Low',
  15: 'Unusual'
}

hydrohraphics = {
  0: '0%-5% Desert world',
  1: '6%-15% Dry world',
  2: '16%-25% A few small seas',
  3: '26%-35% Small seas and oceans',
  4: '36%-45% Wet world',
  5: '46%-55% Large oceans',
  6: '56%-65%',
  7: '66%-75% Earth-like world',
  8: '76%-85% Water world',
  9: '86%-95% Only a few small islands and archipelagos',
  10: '95%-100% Almost entirely water'
}

population = {
  0: 'None',
  1: 'Few',
  2: 'Hundreds',
  3: 'Thousands',
  4: 'Tens of thousands',
  5: 'Hundreds of thousands',
  6: 'Millions',
  7: 'Tens of millions',
  8: 'Hundreds of millions',
  9: 'Billions',
  10: 'Tens of billions',
  11: 'Hundreds of billions',
  12: 'Trillions'
}

techLevel = {
  1: 'Low Tech',
  2: 'Medium Tech',
  3: 'High Tech'
}

government = {
  1: 'Crazy Government',
  2: 'Reasonable Government',
  3: 'Sensible Government'
}

class Planet:
  def __init__( self ):
    self.size = d6() + d6() - 2;
    self.techLevel = random.randint( 1, 3 )
    self.government = random.randint( 1, 3 )

  def __str__( self ):
    return "Size: " + size[self.size] + "\n" + \
           "Tech level: " + techLevel[self.techLevel] + "\n" + \
           "Government: " + government[self.government]

  def planetCode( self ):
    a = "%X" % self.size
    b = ord('A') + self.techLevel - 1
    c = ord('A') + self.government - 1
    return a + chr(b) + chr(c)
 
def main(*args):
  try:
    # program's main code here
    p = Planet()
    print( p )
    print( "Planet code: " + p.planetCode() )
  except:
    # error handling code here
    traceback.print_exc(file=sys.stdout)
    return 1  # exit on error
  else:
    return 0  # exit errorlessly

def d6():
  return random.randint( 1, 6 )

if __name__ == '__main__':
  sys.exit(main(*sys.argv))

