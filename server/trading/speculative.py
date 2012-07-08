commonGoods = ( 'basicElectronics', 'basicMachineParts', 'basicManufacturedGoods',
                'basicRawMaterials', 'basicConsumables', 'basicOre' )
agricultural = ( 'biochemicals', 'liveAnimals', 'luxuryConsumables', 'textiles',
                 'uncommonRawMaterials', 'wood', 'illegalBiochemicals', 'illegalLuxuries' )
asteroid = ( 'crystalsAndGems', 'pharmaceuticals', 'preciousMetals', 'radioactives',
             'uncommonOre', 'illegalDrugs' )
barren = ()
desert = ( 'crystalsAndGems', 'petrochemicals', 'pharmaceuticals', 'preciousMetals',
           'radioactives', 'spices', 'uncommonRawMaterials',
           'illegalDrugs', 'illegalLuxuries' )
fluidOceans = ( 'petrochemicals', 'preciousMetals' )
garden = ( 'liveAnimals', 'luxuryConsumables', 'spices', 'wood' )
highPopulation = ( 'luxuryGoods', 'medicalSupplies', 'pharmaceuticals', 'illegalDrugs' )
highTechnology = ( 'advancedElectronics', 'advancedMachineParts', 'advancedManufacturedGoods',
                   'advancedWeapons', 'advancedVehicles', 'cybernetics', 'medicalSupplies',
                   'robots', 'vehicles', 'illegalWeapons' )
iceCapped = ( 'crystalsAndGems', 'petrochemicals', 'preciousMetals', 'uncommonOre' )
industrial = ( 'advancedElectronics', 'advancedMachineParts', 'advancedManufacturedGoods',
               'advancedWeapons', 'advancedVehicles', 'polymers', 'robots', 'vehicles',
               'illegalWeapons' )
lowPopulation = ( 'radioactives' )
lowTechnology = ()
nonIndustrial = ( 'textiles' )
poor = ()
rich = ()
vacuum = ()
waterWorld = ( 'biochemicals', 'luxuryConsumables', 'petrochemicals', 'pharmaceuticals',
               'spices', 'uncommonRawMaterials', 'illegalBiochemicals', 'illegalDrugs',
               'illegalLuxuries' )

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
}
#13 Basic Manufactured
#Goods
#All 1d6 ∞ 10 10,000 Non-Agricultural +2,
#Industrial +5
#Non-Industrial +3.
#High Population +2
#Household appliances, clothing
#and so forth.
#14 Basic Raw Materials All 1d6 ∞ 10 5,000 Agricultural +3,
#Garden +2
#Industrial +2,
#Poor +2
#Metal, plastics, chemicals and other
#basic materials.
#15 Basic Consumables All 1d6 ∞ 10 2,000 Agricultural +3,
#Water World +2,
#Garden +1,
#Asteroid –4
#Asteroid +1,
#Fluid Oceans +1,
#Ice Capped +1,
#High Population +1
#Food, drink and other agricultural
#products

def determineGoodsAvailable( tradingSpeculative ):
  # roll for common goods
  # determine non-common goods
  # roll for non-common
  # determine illegal goods
  # roll for illegal
  pass
