import unittest
from cities import get_city

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city = get_city('123', 'gou')
        self.assertEqual(city, "123,gou")


unittest.main()
