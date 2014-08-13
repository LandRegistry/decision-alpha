import unittest
import json
from decision import server

class DecisionTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

    def test_server(self):

        rv = self.client.get('/')
        assert rv.status_code == 200

        rv = self.client.get('/decisions')
        assert rv.status_code == 405

        rv = self.client.get('/doesnotexist')
        assert rv.status_code == 404

    def test_change_name(self):

        data = {
                "action": "change-name-marriage",
                "data": {
                    "iso-country-code": "GB"
                },
                "context": {
                    "session-id": "123456",
                    "transaction-id": "ABCDEFG"
                }
            }

        rv = self.client.post('/decisions',
                                data=json.dumps(data),
                                content_type='application/json')

        assert rv.status_code == 200
        assert rv.headers.get('content-type') == 'application/json'
