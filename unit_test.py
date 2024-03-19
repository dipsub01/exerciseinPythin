import unittest
from exercise2 import Vehicle

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.car = Vehicle("Toyota Camry", "ABC123", "Red", "Petrol")

    def test_get_name(self):
        self.assertEqual(self.car.get_name(), "Toyota Camry")

    def test_set_name(self):
        self.car.set_name("Honda Accord")
        self.assertEqual(self.car.get_name(), "Honda Accord")

    def test_get_license_plate(self):
        self.assertEqual(self.car.get_license_plate(), "ABC123")

    def test_set_license_plate(self):
        self.car.set_license_plate("XYZ789")
        self.assertEqual(self.car.get_license_plate(), "XYZ789")

    def test_get_color(self):
        self.assertEqual(self.car.get_color(), "Red")

    def test_set_color(self):
        self.car.set_color("Blue")
        self.assertEqual(self.car.get_color(), "Blue")

    def test_get_fuel_type(self):
        self.assertEqual(self.car.get_fuel_type(), "Petrol")

    def test_set_fuel_type(self):
        self.car.set_fuel_type("Diesel")
        self.assertEqual(self.car.get_fuel_type(), "Diesel")

if __name__ == '__main__':
    unittest.main()
