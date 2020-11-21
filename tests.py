import unittest

import roman_converter

class TestConverter(unittest.TestCase):
    def make_test_set(self):
        self.tests = {
            "I": 1,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6, 
            "IX": 9, 
            "X": 10, 
            "XI": 11, 
            "XIV": 14, 
            "XV": 15,
            "XVI": 16, 
            "XIX": 19, 
            "XX": 20, 
            "XXI": 21, 
            "XXIV": 24,
            "XXV": 25,
            "XXVI": 26,
            "XXIX": 29,
            "XXX": 30,
            "XXXIX": 39,
            "XL": 40,
            "XLI": 41,
            "XLIV": 44,
            "XLV": 45,
            "XLVI": 46,
            "XLIX": 49,
            "L": 50,
            "LI": 51,
            "LIV": 54,
            "LV": 55,
            "LVI": 56,
            "LIX": 59,
            "LX": 60
        }
    
    def test_converter(self):
        self.make_test_set()
        conv = roman_converter.Converter()
        for input, result in self.tests.items():
            converted = conv.convert(input)
            print("Input: " + input + " | Expected: " + str(result) + " | Converted: " + str(converted))
            assert result == converted
        