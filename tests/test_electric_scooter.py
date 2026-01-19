import unittest
from electric_scooter import ElectricScooter

class TestElectricScooter(unittest.TestCase):

    def test_trip_cost_calculation(self):
        scooter = ElectricScooter(1, "Ola", 85, 60)
        cost = scooter.calculate_trip_cost(10)
        self.assertEqual(cost, 1 + (0.15 * 10))

if __name__ == "__main__":
    unittest.main()
