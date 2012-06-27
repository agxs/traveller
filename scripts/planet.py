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

