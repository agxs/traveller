from django.db import models

# Create your models here.

class Planet(models.Model):
  STARPORT_CHOICES = (
    ('X', 'X - No Starport'),
    ('E', 'E - Frontier Starport'),
    ('D', 'D - Poor Starport'),
    ('C', 'C - Routine Starport'),
    ('B', 'B - Good Starport'),
    ('A', 'A - Excellent Starport'),
  )

  SIZE_CHOICES = (
    (0, '0 - 800 km'),
    (1, '1 - 1600 km'),
    (2, '2 - 3200 km'),
    (3, '3 - 4800 km'),
    (4, '4 - 6400 km'),
    (5, '5 - 8000 km'),
    (6, '6 - 9600 km'),
    (7, '7 - 11200 km'),
    (8, '8 - 12800 km'),
    (9, '9 - 14400 km'),
    (10, '10 - 16000 km')
  )

  ATMOSPHERE_CHOICES = (
    (0, '0 - None'),
    (1, '1 - Trace'),
    (2, '2 - Very Thin, Tainted'),
    (3, '3 - Very Thin'),
    (4, '4 - Thin, Tainted'),
    (5, '5 - Thin'),
    (6, '6 - Standard'),
    (7, '7 - Standard, Tainted'),
    (8, '8 - Dense'),
    (9, '9 - Dense, Tainted'),
    (10, '10 - Exotic'),
    (11, '11 - Corrosive'),
    (12, '12 - Insidious'),
    (13, '13 - Dense, High'),
    (14, '14 - Thin, Low'),
    (15, '15 - Unusual')
  )

  TEMPERATURE_CHOICES = (
    (0, '0 - Frozen'),
    (1, '1 - Cold'),
    (2, '2 - Temperate'),
    (3, '3 - Hot'),
    (4, '4 - Roasting'),
  )

  HYDROGRAPHICS_CHOICES = (
    (0, '0 - 0%-5% Desert world'),
    (1, '1 - 6%-15% Dry world'),
    (2, '2 - 16%-25% A few small seas'),
    (3, '3 - 26%-35% Small seas and oceans'),
    (4, '4 - 36%-45% Wet world'),
    (5, '5 - 46%-55% Large oceans'),
    (6, '6 - 56%-65%'),
    (7, '7 - 66%-75% Earth-like world'),
    (8, '8 - 76%-85% Water world'),
    (9, '9 - 86%-95% Only a few small islands and archipelagos'),
    (10, '10 - 95%-100% Almost entirely water')
  )

  POPULATION_CHOICES = (
    (0, '0 - None'),
    (1, '1 - Few'),
    (2, '2 - Hundreds'),
    (3, '3 - Thousands'),
    (4, '4 - Tens of thousands'),
    (5, '5 - Hundreds of thousands'),
    (6, '6 - Millions'),
    (7, '7 - Tens of millions'),
    (8, '8 - Hundreds of millions'),
    (9, '9 - Billions'),
    (10, '10 - Tens of billions'),
    (11, '11 - Hundreds of billions'),
    (12, '12 - Trillions')
  )

  GOVERNMENT_CHOICES = (
    (0, '0 - None'),
    (1, '1 - Company/corporation'),
    (2, '2 - Participating democracy'),
    (3, '3 - Self-perpetuating oligarchy'),
    (4, '4 - Representative democracy'),
    (5, '5 - Feudal technocracy'),
    (6, '6 - Captive government'),
    (7, '7 - Balkanisation'),
    (8, '8 - Civil service bureaucracy'),
    (9, '9 - Impersonal Bureaucracy'),
    (10, '10 - Charismatic dictator'),
    (11, '11 - Non-charismatic leader'),
    (12, '12 - Charismatic oligarchy'),
    (13, '13 - Religious dictatorship'),
  )

  LAW_LEVEL_CHOICES = (
    (0, '0 - No restrictions'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
  )

  TECH_LEVEL_CHOICES = (
    (0, 'TL 0'),
    (1, 'TL 1'),
    (2, 'TL 2'),
    (3, 'TL 3'),
    (4, 'TL 4'),
    (5, 'TL 5'),
    (6, 'TL 6'),
    (7, 'TL 7'),
    (8, 'TL 8'),
    (9, 'TL 9'),
    (10, 'TL 10'),
    (11, 'TL 11'),
    (12, 'TL 12'),
    (13, 'TL 13'),
    (14, 'TL 14'),
    (15, 'TL 15'),
  )

  name = models.CharField( max_length = 64 )
  location = models.CharField( max_length = 8 )
  starport = models.CharField( max_length = 1, choices = STARPORT_CHOICES )
  size = models.IntegerField( choices = SIZE_CHOICES )
  atmosphere = models.IntegerField( choices = ATMOSPHERE_CHOICES )
  temperature = models.IntegerField( choices = TEMPERATURE_CHOICES )
  hydrographics = models.IntegerField( choices = HYDROGRAPHICS_CHOICES )
  population = models.IntegerField( choices = POPULATION_CHOICES )
  government = models.IntegerField( choices = GOVERNMENT_CHOICES )
  law_level = models.IntegerField( choices = LAW_LEVEL_CHOICES )
  tech_level = models.IntegerField( choices = TECH_LEVEL_CHOICES )

  has_gas_giant = models.BooleanField()
  has_naval_base = models.BooleanField()
  has_scout_base = models.BooleanField()
  has_pirate_base = models.BooleanField()
  has_tas = models.BooleanField()
  has_research = models.BooleanField()
  has_consulate = models.BooleanField()

  trade_codes = models.CharField( max_length = 128, blank=True )

  zone = models.CharField( max_length = 1, blank=True )

  notes = models.TextField( blank=True, null=True )

  def toJSON(self):
    return {
      'name': self.name,
      'location': self.location,
      'starport': self.starport,
      'size': self.size,
      'atmosphere': self.atmosphere,
      'temperature': self.temperature,
      'hydrographics': self.hydrographics,
      'population': self.population,
      'government': self.government,
      'law_level': self.law_level,
      'tech_level': self.tech_level,
      'has_gas_giant': self.has_gas_giant,
      'has_naval_base': self.has_naval_base,
      'has_scout_base': self.has_scout_base,
      'has_pirate_base': self.has_pirate_base,
      'has_tas': self.has_tas,
      'has_research': self.has_research,
      'has_consulate': self.has_consulate,
      'trade_codes': self.trade_codes,
      'zone': self.zone,
      'notes': self.notes,
    }

  def __unicode__(self):
    return self.location + " - " + self.name
