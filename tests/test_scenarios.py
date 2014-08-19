import unittest
from decision.scenarios import *

class CheckChangeNameMarriage(unittest.TestCase):

    def test_given_data_with_uppercase_gb_returns_true(self):
        self.assertTrue(check_change_name_marriage({"iso-country-code": "GB"}))

    def test_given_data_with_lowercase_gb_returns_false(self):
        self.assertFalse(check_change_name_marriage({"iso-country-code": "gb"}))

    def test_given_data_with_aq_returns_false(self):
        self.assertFalse(check_change_name_marriage({"iso-country-code": "AQ"}))

    def test_given_data_with_none_returns_false(self):
        self.assertFalse(check_change_name_marriage({"iso-country-code": None}))

    def test_given_no_data_return_false(self):
        self.assertRaises(AttributeError, check_change_name_marriage, None)



