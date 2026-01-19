import unittest
from electric_car import ElectricCar

class TestElectricCar(unittest.TestCase):

    def test_trip_cost_calculation(self):
        car = ElectricCar(1, "Tesla", 90, 5)
        cost = car.calculate_trip_cost(10)
        self.assertEqual(cost, 5 + (0.5 * 10))

if __name__ == "__main__":
    unittest.main()
