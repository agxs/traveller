from utils.dice import parseDiceExpr
from planetserve.models import Planet
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger( __name__ )

trade_code_with_goods = {
  'common_goods': ( 'basicElectronics', 'basicMachineParts', 'basicManufacturedGoods',
                   'basicRawMaterials', 'basicConsumables', 'basicOre' ),
  'Ag': ( 'biochemicals', 'liveAnimals', 'luxuryConsumables', 'textiles',
          'uncommonRawMaterials', 'wood', 'illegalBiochemicals', 'illegalLuxuries' ),
  'As': ( 'crystalsAndGems', 'pharmaceuticals', 'preciousMetals', 'radioactives',
          'uncommonOre', 'illegalDrugs' ),
  'Ba': (),
  'De': ( 'crystalsAndGems', 'petrochemicals', 'pharmaceuticals', 'preciousMetals',
          'radioactives', 'spices', 'uncommonRawMaterials',
          'illegalDrugs', 'illegalLuxuries' ),
  'Fl': ( 'petrochemicals', 'preciousMetals' ),
  'Ga': ( 'liveAnimals', 'luxuryConsumables', 'spices', 'wood' ),
  'Hi': ( 'luxuryGoods', 'medicalSupplies', 'pharmaceuticals', 'illegalDrugs' ),
  'Ht': ( 'advancedElectronics', 'advancedMachineParts', 'advancedManufacturedGoods',
          'advancedWeapons', 'advancedVehicles', 'cybernetics', 'medicalSupplies',
          'robots', 'vehicles', 'illegalWeapons' ),
  'Ic': ( 'crystalsAndGems', 'petrochemicals', 'preciousMetals', 'uncommonOre' ),
  'In': ( 'advancedElectronics', 'advancedMachineParts', 'advancedManufacturedGoods',
          'advancedWeapons', 'advancedVehicles', 'polymers', 'robots', 'vehicles',
          'illegalWeapons' ),
  'Lo': ( 'radioactives' ),
  'Lt': (),
  'Ni': ( 'textiles' ),
  'Po': (),
  'Ri': (),
  'Va': (),
  'Wa': ( 'biochemicals', 'luxuryConsumables', 'petrochemicals', 'pharmaceuticals',
          'spices', 'uncommonRawMaterials', 'illegalBiochemicals', 'illegalDrugs',
          'illegalLuxuries' ),
  'G': (),
  'A': (),
  'R': (),
}

trade_lookup = {
  11: 'basicElectronics',
  12: 'basicMachineParts',
  13: 'basicManufacturedGoods',
  14: 'basicRawMaterials',
  15: 'basicConsumables',
  16: 'basicOre',
  21: 'advancedElectronics',
  22: 'advancedMachineParts',
  23: 'advancedManufacturedGoods',
  24: 'advancedWeapons',
  25: 'advancedVehicles',
  26: 'biochemicals',
  31: 'crystalsAndGems',
  32: 'cybernetics',
  33: 'liveAnimals',
  34: 'luxuryConsumables',
  35: 'luxuryGoods',
  36: 'medicalSupplies',
  41: 'petrochemicals',
  42: 'pharmaceuticals',
  43: 'polymers',
  44: 'preciousMetals',
  45: 'radioactives',
  46: 'robots',
  51: 'spices',
  52: 'textiles',
  53: 'uncommonOre',
  54: 'uncommonRawMaterials',
  55: 'wood',
  56: 'vehicles',
  61: 'illegalBiochemicals',
  62: 'illegalCybernetics',
  63: 'illegalDrugs',
  64: 'illegalLuxuries',
  65: 'illegalWeapons',
}

class TradeGood():
  def __init__( self, name, availability, cost, purchase, sale, illegal ):
    self.name = name
    self.availability = availability
    self.cost = cost
    self.purchase = purchase
    self.sale = sale
    self.illegal = illegal

trade_goods = {
  'basicElectronics':
    TradeGood( 'Basic Electronics', '1d6*10', 10000, {
      'In': 2,
      'Ht': 3,
      'Ri': 1,
    }, {
      'Ni': 2,
      'Lo': 1,
      'Po': 1,
    }, False ),
  'basicMachineParts':
    TradeGood( 'Basic Machine Parts', '1d6*10', 10000, {
      'Na': 2,
      'In': 5,
    }, {
      'Na': 3,
      'Ag': 2,
    }, False ),
  'basicManufacturedGoods':
    TradeGood( 'Basic Manufactured Goods', '1d6*10', 10000, {
      'Na': 2,
      'In': 5,
    }, {
      'Ni': 3,
      'Hi': 2,
    }, False ),
  'basicRawMaterials':
    TradeGood( 'Basic Raw Materials', '1d6*10', 5000, {
      'Ag': 3,
      'Ga': 2,
    }, {
      'In': 2,
      'Po': 2,
    }, False ),
  'basicConsumables':
    TradeGood( 'Basic Consumables', '1d6*10', 2000, {
      'Ag': 3,
      'Wa': 2,
      'Ga': 1,
      'As': -4,
    }, {
      'As': 1,
      'Fl': 1,
      'Ic': 1,
      'Hi': 1,
    }, False ),
  'basicOre':
    TradeGood( 'Basic Ore', '1d6*10', 1000, {
      'As': 4,
    }, {
      'In': 3,
      'Ni': 1,
    }, False ),
  'advancedElectronics':
    TradeGood( 'Advanced Electronics', '1d6*5', 100000, {
      'In': 2,
      'Ht': 3,
    }, {
      'Ni': 1,
      'Ri': 2,
      'As': 3,
    }, False ),
  'advancedMachineParts':
    TradeGood( 'Advanced Machine Parts', '1d6*5', 75000, {
      'In': 2,
      'Ht': 1,
    }, {
      'As': 2,
      'Ni': 1,
    }, False ),
  'advancedManufacturedGoods':
    TradeGood( 'Advanced Manufactured Goods', '1d6*5', 100000, {
      'In': 1,
    }, {
      'Hi': 1,
      'Ri': 2,
    }, False ),
  'advancedWeapons':
    TradeGood( 'Advanced Weapons', '1d6*5', 150000, {
      'Ht': 2,
    }, {
      'Po': 1,
      'A': 2,
      'R': 4,
    }, False ),
  'advancedVehicles':
    TradeGood( 'Advanced Vehicles', '1d6*5', 180000, {
      'Ht': 2,
    }, {
      'As': 2,
      'Ri': 2,
    }, False ),
  'biochemicals':
    TradeGood( 'Biochemicals', '1d6*5', 50000, {
      'Ag': 1,
      'Wa': 2,
    }, {
      'In': 2,
    }, False ),
  'crystalsAndGems':
    TradeGood( 'Crystals And Gems', '1d6*5', 20000, {
      'As': 2,
      'De': 1,
      'Ic': 1,
    }, {
      'In': 3,
      'Ri': 2,
    }, False ),
  'cybernetics':
    TradeGood( 'Cybernetics', '1d6', 10000, {
    }, {
      'Ht': 1,
      'Ic': 1,
      'Ri': 2,
    }, False ),
  'liveAnimals':
    TradeGood( 'Live Animals', '1d6*10', 10000, {
      'Ag': 2,
    }, {
      'Lo': 3,
    }, False ),
  'luxuryConsumables':
    TradeGood( 'Luxury Consumables', '1d6*10', 20000, {
      'Ag': 2,
      'Wa': 1,
    }, {
      'Ri': 2,
      'Hi': 2,
    }, False ),
  'luxuryGoods':
    TradeGood( 'Luxury Goods', '1d6', 200000, {
    }, {
      'Ri': 4,
    }, False ),
  'medicalSupplies':
    TradeGood( 'Medical Supplies', '1d6*5', 50000, {
      'Ht': 2,
    }, {
      'In': 2,
      'Po': 1,
      'Ri': 1,
    }, False ),
  'petrochemicals':
    TradeGood( 'Petrochemicals', '1d6', 100000, {
      'De': 2,
    }, {
      'In': 2,
      'Ag': 1,
      'Lo': 2
    }, False ),
  'pharmaceuticals':
    TradeGood( 'Pharmaceuticals', '1d6', 100000, {
      'As': 2,
      'Hi': 1,
    }, {
      'Ri': 2,
      'Lo': 1,
    }, False ),
  'polymers':
    TradeGood( 'Polymers', '1d6*10', 7000, {
    }, {
      'Ri': 2,
      'Ni': 1,
    }, False ),
  'preciousMetals':
    TradeGood( 'Precious Metals', '1d6', 50000, {
      'As': 3,
      'De': 1,
      'Ic': 2,
    }, {
      'Ri': 3,
      'In': 2,
      'Ht': 1
    }, False ),
  'radioactives':
    TradeGood( 'Radioactives', '1d6', 1000000, {
      'As': 2,
      'Lo': -4,
    }, {
      'In': 3,
      'Ht': 1,
      'Ni': -2,
      'Ag': -3,
    }, False ),
  'robots':
    TradeGood( 'Robots', '1d6*5', 400000, {
    }, {
      'Ag': 2,
      'Ht': 1,
    }, False ),
  'spices':
    TradeGood( 'Spices', '1d6*5', 6000, {
      'De': 2,
    }, {
      'Hi': 2,
      'Ri': 3,
      'Po': 3,
    }, False ),
  'textiles':
    TradeGood( 'Textiles', '1d6*10', 3000, {
      'Ag': 7,
    }, {
      'Hi': 3,
      'Na': 2,
    }, False ),
  'uncommonOre':
    TradeGood( 'Uncommon Ore', '1d6*10', 5000, {
      'As': 4,
    }, {
      'In': 3,
      'Ni': 1,
    }, False ),
  'uncommonRawMaterials':
    TradeGood( 'Uncommon Raw Materials', '1d6*10', 20000, {
      'Ag': 2,
    }, {
      'In': 2,
      'Ht': 1,
    }, False ),
  'wood':
    TradeGood( 'Wood', '1d6*10', 1000, {
      'Ag': 6,
    }, {
      'Ri': 2,
      'In': 1,
    }, False ),
  'vehicles':
    TradeGood( 'Vehicles', '1d6*10', 15000, {
      'In': 2,
      'Ht': 1,
    }, {
      'Ni': 2,
      'Hi': 1,
    }, False ),
  'illegalBiochemicals':
    TradeGood( 'Illegal Biochemicals', '1d6*5', 50000, {
      'Wa': 2,
    }, {
      'In': 6,
    }, True ),
  'illegalCybernetics':
    TradeGood( 'Illegal Cybernetics', '1d6', 250000, {
    }, {
      'As': 4,
      'Ic': 4,
      'Ri': 8,
      'A': 6,
      'R': 6,
    }, True ),
  'illegalDrugs':
    TradeGood( 'Illegal Drugs', '1d6', 100000, {
    }, {
      'Ri': 6,
      'Hi': 6,
    }, True ),
  'illegalLuxuries':
    TradeGood( 'Illegal Luxuries', '1d6', 50000, {
      'Ag': 2,
      'Wa': 1,
    }, {
      'Ri': 6,
      'Hi': 4,
    }, True ),
  'illegalWeapons':
    TradeGood( 'Illegal Weapons', '1d6*5', 150000, {
      'Ht': 2,
    }, {
      'Po': 6,
      'A': 8,
      'R': 10,
    }, True ),
}
'''
template
  '':
    TradeGood( '', '', 0, {
      '': 0,
      '': 0,
    }, {
      '': 0,
      '': 0,
    } ),
'''

def determineGoodsAvailable( tradingCore, tradingSpeculative ):

  startPlanet = get_object_or_404( Planet, location__exact=tradingCore['startPlanet'] )
  availableGoods = {}

  merchantGoods = trade_code_with_goods['common_goods']
  for t in startPlanet.generateTradeCode().split( " " ):
    merchantGoods += trade_code_with_goods[t]

  extra_goods = parseDiceExpr( "1d6" )
  for _ in range( extra_goods ):
    # no do-while in python?
    while True:
      tens = parseDiceExpr( "1d6" )
      units = parseDiceExpr( "1d6" )
      dice_total = tens * 10 + units
      # roll again on 66
      if dice_total < 66:
        break;
    merchantGoods += ( trade_lookup[dice_total], )

  for c in merchantGoods:
    item = trade_goods[c]
    if c not in availableGoods:
      availableGoods[c] = {
        'display': item.name,
        'cost': item.cost,
        'availability': parseDiceExpr( item.availability ),
        'purchaseDm': tradingSpeculative['broker'] + \
                      tradingSpeculative['intOrSocial'] + \
                      __calcGoodsDM( item.purchase, startPlanet ) - \
                      __calcGoodsDM( item.sale, startPlanet ),
        'illegal': item.illegal
      }
    else:
      availableGoods[c]['availability'] += parseDiceExpr( item.availability )
  # filter illegal goods
  return availableGoods

# Calculates the purchase/sale DM for each trade good.
# trade_codes is a list of planet trade codes which the trade good has
# planet is the Planet where the purchase/sale is occuring
def __calcGoodsDM( trade_codes, planet ):
  dms = set( trade_codes ).intersection( planet.generateTradeCode().split( " " ) )
  maxDm = 0
  for p in dms:
    if trade_codes[p] > maxDm:
      maxDm = trade_codes[p]
  logger.info( str( dms ) + " " + str( maxDm ) )

  return maxDm

def negotiateTradeTood( item ):
  pass
