import unittest

from AirlineProfit import Ticket, Fuel, Staff, Airplane, Flight, Air_company

class AirlineProfitTest(unittest.TestCase):
    def test_set_ticket_price(self):
        ticket = Ticket(450)
        self.assertEqual(ticket.price, 450)
    def test_set_fuel_price(self):
        fuel = Fuel(0.52)
        self.assertEqual(fuel.price, 0.52)
    def test_set_crew_salarie(self):
        crew = Staff(2600)
        self.assertEqual(crew.salary, 2600)
    def test_setup_plane(self):
        boeing_777 = Airplane(314, 0, 6800)
        self.assertEqual(boeing_777.capasity, 314)
        self.assertEqual(boeing_777.consumption, 6800)
    def test_flight_setup(self):
        flight682 = Flight(10)
        self.assertEqual(flight682.distance, 10)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    all_tests_from_class = loader.loadTestsFromTestCase(AirlineProfitTest)
    unittest.TextTestRunner(verbosity=2).run(all_tests_from_class)