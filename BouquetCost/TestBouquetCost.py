import unittest

from BouquetCost import Bouquet, BouquetItem


class BouquetCostTest(unittest.TestCase):
    def test_set_bouquet_item(self):
        tulip = BouquetItem('tulip',1.25)
        self.assertEqual(tulip.name_price, ['tulip',1.25])
    def test_setup_bouquet(self):
        tulip_bouquet = Bouquet()
        self.assertEqual(tulip_bouquet.content, [])
        self.assertEqual(tulip_bouquet.price, 0)
    def test_add_item_to_bouquet(self):
        tulip = BouquetItem('tulip',1.25)
        tulip_bouquet = Bouquet()
        tulip_bouquet.add(tulip,3)
        self.assertEqual(tulip_bouquet.content, [['tulip',1.25,3]])
    def test_calculate_bouquet_cost(self):
        tulip = BouquetItem('tulip',1.25)
        tulip_bouquet = Bouquet()
        tulip_bouquet.add(tulip,3)
        tulip_bouquet.calculate_cost()
        self.assertEqual(tulip_bouquet.price, 3.75)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    all_tests_from_class = loader.loadTestsFromTestCase(BouquetCostTest)
    unittest.TextTestRunner(verbosity=2).run(all_tests_from_class)