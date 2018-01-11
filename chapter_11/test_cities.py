import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

def test_city_country(self):
    """does a simple city and country pair work?"""
    santiago_chili = city_country('santiago', 'chile')
    self.assertEqual(santiago_chile, 'Santiago, Chile')

unittest.main()
