#!/usr/bin/env python

import sys
import traceback
import random

size = {
  1: 'Small Size',
  2: 'Medium Size',
  3: 'Large Size'
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
    self.size = random.randint( 1, 3 )
    self.techLevel = random.randint( 1, 3 )
    self.government = random.randint( 1, 3 )

  def __str__( self ):
    return "Size: " + size[self.size] + "\n" + \
           "Tech level: " + techLevel[self.techLevel] + "\n" + \
           "Government: " + government[self.government]

  def planetCode( self ):
    a = ord('A') + self.size - 1
    b = ord('A') + self.techLevel - 1
    c = ord('A') + self.government - 1
    return chr(a) + chr(b) + chr(c)
 
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

if __name__ == '__main__':
  sys.exit(main(*sys.argv))

