import unittest
from electric_car import ElectricCar

class TestVehicle(unittest.TestCase):

    def test_valid_battery_percentage(self):
        car = ElectricCar(1, "Tesla", 80, 5)
        self.assertEqual(car.get_battery_percentage(), 80)

    def test_invalid_battery_percentage(self):
        with self.assertRaises(ValueError):
            ElectricCar(2, "BMW", 150, 4)

    def test_default_maintenance_status(self):
        car = ElectricCar(3, "Audi", 70, 4)
        self.assertEqual(car.get_maintenance_status(), "Available")

    def test_set_valid_maintenance_status(self):
        car = ElectricCar(4, "Nexon", 60, 5)
        car.set_maintenance_status("On Trip")
        self.assertEqual(car.get_maintenance_status(), "On Trip")

    def test_invalid_maintenance_status(self):
        car = ElectricCar(5, "Kia", 60, 5)
        with self.assertRaises(ValueError):
            car.set_maintenance_status("Broken")

if __name__ == "__main__":
    unittest.main()
