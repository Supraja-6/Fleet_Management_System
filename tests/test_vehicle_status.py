import unittest
from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from vehicle import Vehicle

class TestVehicleAdvanced(unittest.TestCase):

    def test_vehicle_equality(self):
        car1 = ElectricCar(1, "Tesla", 80, 5)
        car2 = ElectricCar(1, "Tesla", 70, 4)
        self.assertEqual(car1, car2)

    def test_vehicle_not_equal(self):
        car1 = ElectricCar(1, "Tesla", 80, 5)
        car2 = ElectricCar(2, "Tesla", 80, 5)
        self.assertNotEqual(car1, car2)

    def test_string_representation(self):
        car = ElectricCar(10, "BMW", 90, 4)
        self.assertIn("Vehicle ID: 10", str(car))
        self.assertIn("BMW", str(car))

    def test_abstract_vehicle_instantiation(self):
        with self.assertRaises(TypeError):
            Vehicle(1, "Test", 50)
