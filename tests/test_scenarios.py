import unittest
from decision.scenarios import *

class CheckChangeNameMarriage(unittest.TestCase):

    def test_given_data_with_uppercase_gb_returns_true(self):
        data = {"iso-country-code": "GB"}
        self.assertTrue(check_change_name_marriage(data))

    def test_given_data_with_lowercase_gb_returns_false(self):
        data = {"iso-country-code": "gb"}
        self.assertFalse(check_change_name_marriage(data))

    def test_given_data_with_aq_returns_false(self):
        data = {"iso-country-code": "AQ"}
        self.assertFalse(check_change_name_marriage(data))

    def test_given_data_with_none_returns_false(self):
        data = {"iso-country-code": None}
        self.assertFalse(check_change_name_marriage(data))

    def test_given_no_data_return_false(self):
        self.assertRaises(AttributeError, check_change_name_marriage, None)



