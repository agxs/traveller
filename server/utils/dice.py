'''
Created on 7 Jul 2012

@author: agxs
'''
import random

# Parses a string expression representing a dice roll. For example "1+2d6" will
# roll 2 d6s then add 1. Valid operators are + and -. To write -1, do "0-1".
# Any integer is recognised for the number of dice, and the dice type. Eg,
# "3d60" will roll 3 d60s. Any size of expression can be parsed, so even complex
# expressions such as "3+4d6-2-4+2+5d20" etc will work.
def parseDiceExpr( expr ):
  e = __Expr()
  e.str = expr
  
  t = __lexDiceExpr( e )
  value = __evalLiteral( t )
  t = __lexDiceExpr( e )
  while ( t.type != __Token.END ):
    if ( t.type == __Token.PLUS ):
      value += __evalLiteral( __lexDiceExpr( e ) )
    elif ( t.type == __Token.MINUS ):
      value -= __evalLiteral( __lexDiceExpr( e ) )
    else:
      raise Exception( 'Parse error, unknown operator at ', t.position )
    t = __lexDiceExpr( e )
  
  return value

# Returns the real value of the two possible literals(integer or dice)
def __evalLiteral( t ):
  if ( t.type == __Token.INT ):
    return t.value
  elif ( t.type == __Token.DICE ):
    diceValue = 0
    while t.numDice > 0:
      diceValue += random.randint( 1, t.diceType )
      t.numDice -= 1
    return diceValue
  else:
    raise Exception( 'Parse error, unknown literal at ', t.position )

# Lexes the supplied expression and returns a __Token representing the
# character at the position in the __Expr object
def __lexDiceExpr( expr ):
  t = __Token()
  
  if ( expr.position >= len( expr.str ) ):
    t.type = __Token.END
  elif ( __isDigit( expr.str[expr.position] ) ):
    newStr = expr.str[expr.position]
    diceStr = ""
    t.type = __Token.INT
    t.position = expr.position
    expr.position += 1
    while ( expr.position < len( expr.str ) and \
            not __isOperator( expr.str[expr.position] ) ):
      if ( __isDigit( expr.str[expr.position] ) ):
        newStr += expr.str[expr.position]
        expr.position += 1
      elif ( expr.str[expr.position] == "d" ):
        expr.position += 1
        while ( expr.position < len( expr.str ) and \
                not __isOperator( expr.str[expr.position] ) ) :
          diceStr += expr.str[expr.position]
          expr.position += 1
        t.type = __Token.DICE
        t.numDice = int( newStr )
        t.diceType = int( diceStr )
      else:
        break;
    
    t.value = int( newStr )
  elif ( expr.str[expr.position] == '+' ):
    t.type = __Token.PLUS
    t.position = expr.position
    expr.position += 1
  elif ( expr.str[expr.position] == '-' ):
    t.type = __Token.MINUS
    t.position = expr.position
    expr.position += 1
  else:
    raise Exception( 'Invalid token', expr.str[expr.position] )
  
  return t

# Checks to see if the supplied character is an integer
def __isDigit( c ):
  try:
    int(c)
    return True
  except ValueError:
    return False

# Checks to see if the supplied character is a valid operator( + or - )
def __isOperator( c ):
  return c == "+" or c == "-"

# Represents a lexical token
class __Token:
  NONE = 0
  INT = 1
  PLUS = 2
  MINUS = 3
  DICE = 4
  END = 5
  
  type = NONE
  value = 0
  numDice = 0
  diceType = 0
  position = 0

# Represents the expression being parsed and the position of the parser
class __Expr:
  str = ""
  position = 0
