import unittest
import temperature_converter as tc

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(tc.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(tc.celsius_to_fahrenheit(100), 212)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(tc.celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(tc.celsius_to_kelvin(-273.15), 0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(tc.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(tc.fahrenheit_to_celsius(212), 100)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(tc.fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(tc.fahrenheit_to_kelvin(-459.67), 0, places=2)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(tc.kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(tc.kelvin_to_celsius(0), -273.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(tc.kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(tc.kelvin_to_fahrenheit(0), -459.67, places=2)

    def test_convert_temperature(self):
        self.assertEqual(tc.convert_temperature(0, 'C'), "0°C = 32.00°F = 273.15K")
        self.assertEqual(tc.convert_temperature(32, 'F'), "32°F = 0.00°C = 273.15K")
        self.assertEqual(tc.convert_temperature(273.15, 'K'), "273.15K = 0.00°C = 32.00°F")
        self.assertEqual(tc.convert_temperature(100, 'X'), "Invalid scale! Use 'C', 'F', or 'K'.")

if __name__ == '__main__':
    unittest.main()
