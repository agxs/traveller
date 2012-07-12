from utils.dice import parseDiceExpr
from planetserve.models import Planet
from django.shortcuts import get_object_or_404

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
  def __init__( self, name, availability, cost, purchase, sale ):
    self.name = name
    self.availability = availability
    self.cost = cost
    self.purchase = purchase
    self.sale = sale

trade_goods = {
  'basicElectronics':
    TradeGood( 'basicElectronics', '1d6*10', 10000, {
      'In': 2,
      'Ht': 3,
      'Ri': 1,
    }, {
      'Ni': 2,
      'Lo': 1,
      'Po': 1,
    } ),
  'basicMachineParts':
    TradeGood( 'basicMachineParts', '1d6*10', 10000, {
      'Na': 2,
      'In': 5,
    }, {
      'Na': 3,
      'Ag': 2,
    } ),
  'basicManufacturedGoods':
    TradeGood( 'basicManufacturedGoods', '1d6*10', 10000, {
      'Na': 2,
      'In': 5,
    }, {
      'Ni': 3,
      'Hi': 2,
    } ),
  'basicRawMaterials':
    TradeGood( 'basicRawMaterials', '1d6*10', 5000, {
      'Ag': 3,
      'Ga': 2,
    }, {
      'In': 2,
      'Po': 2,
    } ),
  'basicConsumables':
    TradeGood( 'basicConsumables', '1d6*10', 2000, {
      'Ag': 3,
      'Wa': 2,
      'Ga': 1,
      'As': -4,
    }, {
      'As': 1,
      'Fl': 1,
      'Ic': 1,
      'Hi': 1,
    } ),
  'basicOre':
    TradeGood( 'basicOre', '1d6*10', 1000, {
      'As': 4,
    }, {
      'In': 3,
      'Ni': 1,
    } ),
  'advancedElectronics':
    TradeGood( 'advancedElectronics', '1d6*5', 100000, {
      'In': 2,
      'Ht': 3,
    }, {
      'Ni': 1,
      'Ri': 2,
      'As': 3,
    } ),
  'advancedMachineParts':
    TradeGood( 'advancedMachineParts', '1d6*5', 75000, {
      'In': 2,
      'Ht': 1,
    }, {
      'As': 2,
      'Ni': 1,
    } ),
  'advancedManufacturedGoods':
    TradeGood( 'advancedManufacturedGoods', '1d6*5', 100000, {
      'In': 1,
    }, {
      'Hi': 1,
      'Ri': 2,
    } ),
  'advancedWeapons':
    TradeGood( 'advancedWeapons', '1d6*5', 150000, {
      'Ht': 2,
    }, {
      'Po': 1,
      'A': 2,
      'R': 4,
    } ),
  'advancedVehicles':
    TradeGood( 'advancedVehicles', '1d6*5', 180000, {
      'Ht': 2,
    }, {
      'As': 2,
      'Ri': 2,
    } ),
  'biochemicals':
    TradeGood( 'biochemicals', '1d6*5', 50000, {
      'Ag': 1,
      'Wa': 2,
    }, {
      'In': 2,
    } ),
  'crystalsAndGems':
    TradeGood( 'crystalsAndGems', '1d6*5', 20000, {
      'As': 2,
      'De': 1,
      'Ic': 1,
    }, {
      'In': 3,
      'Ri': 2,
    } ),
  'cybernetics':
    TradeGood( 'cybernetics', '1d6', 10000, {
    }, {
      'Ht': 1,
      'Ic': 1,
      'Ri': 2,
    } ),
  'liveAnimals':
    TradeGood( 'liveAnimals', '1d6*10', 10000, {
      'Ag': 2,
    }, {
      'Lo': 3,
    } ),
  'luxuryConsumables':
    TradeGood( 'luxuryConsumables', '1d6*10', 20000, {
      'Ag': 2,
      'Wa': 1,
    }, {
      'Ri': 2,
      'Hi': 2,
    } ),
  'luxuryGoods':
    TradeGood( 'luxuryGoods', '1d6', 200000, {
    }, {
      'Ri': 4,
    } ),
  'medicalSupplies':
    TradeGood( 'medicalSupplies', '1d6*5', 50000, {
      'Ht': 2,
    }, {
      'In': 2,
      'Po': 1,
      'Ri': 1,
    } ),
  'petrochemicals':
    TradeGood( 'petrochemicals', '1d6', 100000, {
      'De': 2,
    }, {
      'In': 2,
      'Ag': 1,
      'Lo': 2
    } ),
  'pharmaceuticals':
    TradeGood( 'pharmaceuticals', '1d6', 100000, {
      'As': 2,
      'Hi': 1,
    }, {
      'Ri': 2,
      'Lo': 1,
    } ),
  'polymers':
    TradeGood( 'polymers', '1d6*10', 7000, {
    }, {
      'Ri': 2,
      'Ni': 1,
    } ),
  'preciousMetals':
    TradeGood( 'preciousMetals', '1d6', 50000, {
      'As': 3,
      'De': 1,
      'Ic': 2,
    }, {
      'Ri': 3,
      'In': 2,
      'Ht': 1
    } ),
  'radioactives':
    TradeGood( 'radioactives', '1d6', 1000000, {
      'As': 2,
      'Lo': -4,
    }, {
      'In': 3,
      'Ht': 1,
      'Ni': -2,
      'Ag': -3,
    } ),
  'robots':
    TradeGood( 'robots', '1d6*5', 400000, {
    }, {
      'Ag': 2,
      'Ht': 1,
    } ),
  'spices':
    TradeGood( 'spices', '1d6*5', 6000, {
      'De': 2,
    }, {
      'Hi': 2,
      'Ri': 3,
      'Po': 3,
    } ),
  'textiles':
    TradeGood( 'textiles', '1d6*10', 3000, {
      'Ag': 7,
    }, {
      'Hi': 3,
      'Na': 2,
    } ),
  'uncommonOre':
    TradeGood( 'uncommonOre', '1d6*10', 5000, {
      'As': 4,
    }, {
      'In': 3,
      'Ni': 1,
    } ),
  'uncommonRawMaterials':
    TradeGood( 'uncommonRawMaterials', '1d6*10', 20000, {
      'Ag': 2,
    }, {
      'In': 2,
      'Ht': 1,
    } ),
  'wood':
    TradeGood( 'wood', '1d6*10', 1000, {
      'Ag': 6,
    }, {
      'Ri': 2,
      'In': 1,
    } ),
  'vehicles':
    TradeGood( 'vehicles', '1d6*10', 15000, {
      'In': 2,
      'Ht': 1,
    }, {
      'Ni': 2,
      'Hi': 1,
    } ),
  'illegalBiochemicals':
    TradeGood( 'illegalBiochemicals', '1d6*5', 50000, {
      'Wa': 2,
    }, {
      'In': 6,
    } ),
  'illegalCybernetics':
    TradeGood( 'illegalCybernetics', '1d6', 250000, {
    }, {
      'As': 4,
      'Ic': 4,
      'Ri': 8,
      'A': 6,
      'R': 6,
    } ),
  'illegalDrugs':
    TradeGood( 'illegalDrugs', '1d6', 100000, {
    }, {
      'Ri': 6,
      'Hi': 6,
    } ),
  'illegalLuxuries':
    TradeGood( 'illegalLuxuries', '1d6', 50000, {
      'Ag': 2,
      'Wa': 1,
    }, {
      'Ri': 6,
      'Hi': 4,
    } ),
  'illegalWeapons':
    TradeGood( 'illegalWeapons', '1d6*5', 150000, {
      'Ht': 2,
    }, {
      'Po': 6,
      'A': 8,
      'R': 10,
    } ),
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

  for c in merchantGoods:
    item = trade_goods[c]
    if item.name not in availableGoods:
      availableGoods[item.name] = {
        'cost': item.cost,
        'availability': parseDiceExpr( item.availability ),
        # purchase dm
      }
    else:
      availableGoods[item.name].availablity += parseDiceExpr( item.availability )
  # roll for common goods
  # determine non-common goods
  # roll for non-common
  # determine illegal goods
  # roll for illegal
  return availableGoods
