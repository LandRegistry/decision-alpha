import unittest
from decision.scenarios import *

class CheckChangeNameMarriage(unittest.TestCase):

    def test_given_data_with_uppercase_gb_returns_true(self):
        data = {"iso-country-code": "GB"}
        result = check_change_name_marriage(data)
        assert result == True

    def test_given_data_with_lowercase_gb_returns_false(self):
        data = {"iso-country-code": "gb"}
        result = check_change_name_marriage(data)
        assert result == False

    def test_given_data_with_aq_returns_false(self):
        data = {"iso-country-code": "AQ"}
        result = check_change_name_marriage(data)
        assert result == False

    def test_given_data_with_none_returns_false(self):
        data = {"iso-country-code": None}
        result = check_change_name_marriage(data)
        assert result == False

    def test_given_no_data_return_false(self):
        try:
            data = None
            result = check_change_name_marriage(data)
            assert False
        except AttributeError:
            assert True
            


