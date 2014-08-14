import unittest
import json
from decision import server, app
from decision import decision_service

class DecisionServiceTestCase(unittest.TestCase):   
    
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = app

    def test_perform_action_returns_200_and_send_to_casework_response_when_data_present_and_check_is_true(self):
        with self.app.test_request_context():
            valid_data = {
                        "action": "change-name-marriage",
                        "data": {
                            "iso-country-code": "GB"
                        },
                        "context": {
                            "session-id": "123456",
                            "transaction-id": "ABCDEFG"
                        }
                    }

            action_response = decision_service.perform_action(valid_data)
            assert action_response.status_code == 200
            assert json.loads(action_response.data) == { "action": "send-to-casework", "signed-token": "1234", "transaction-id": "ABCDEFG"  }
    
    def test_perform_action_returns_200_and_send_to_check_when_country_code_is_not_GB(self):
         with self.app.test_request_context():
            bad_data = {
                    "action": "change-name-marriage",
                    "data": {
                         "iso-country-code": "not valid"
                    },
                    "context": {
                        "session-id": "123456",
                        "transaction-id": "ABCDEFG"
                    }
                }
            action_response = decision_service.perform_action(bad_data)
            assert action_response.status_code == 200
            assert json.loads(action_response.data) == { "action": "send-to-check", "signed-token": "1234", "transaction-id": "ABCDEFG"  }

    def test_perform_action_returns_200_and_send_to_check_when_missing_country_code(self):
         with self.app.test_request_context():
            bad_data = {
                    "action": "change-name-marriage",
                    "data": {
                        "iso-country-code": None
                    },
                    "context": {
                        "session-id": "123456",
                        "transaction-id": "ABCDEFG"
                    }
                }
            action_response = decision_service.perform_action(bad_data)
            assert action_response.status_code == 200
            assert json.loads(action_response.data) == { "action": "send-to-check", "signed-token": "1234", "transaction-id": "ABCDEFG"  }

    def test_perform_action_returns_400_when_data_is_missing(self):
         with self.app.test_request_context():
            bad_data = {
                    "action": "change-name-marriage",
                    "no-data": {
                        "something": "invalid"
                    },
                    "context": {
                        "session-id": "123456",
                        "transaction-id": "ABCDEFG"
                    }
                }
            action_response = decision_service.perform_action(bad_data)
            assert action_response.status_code == 400
            assert json.loads(action_response.data) == {'error_message': 'Missing country code' }

    def test_perform_action_returns_400_when_action_is_not_valid(self):
        with self.app.test_request_context():
            bad_data = {
                   "action": "action-is-invalid",
                   "data": {
                            "iso-country-code": "GB"
                    },
                    "context": {
                        "session-id": "123456",
                        "transaction-id": "ABCDEFG"
                    }
                }
            action_response = decision_service.perform_action(bad_data)
            assert action_response.status_code == 400
            assert json.loads(action_response.data) == {'error_message': 'Action not found' }

    

    def test_make_error_response_returns_bad_request_response_with_given_message(self):
        with self.app.test_request_context():
            msg = 'some random message'
            err = decision_service.make_error_response(msg)
            assert err.status_code == 400
            assert json.loads(err.data) == { 'error_message' : msg }
        
