import unittest
import json
from decision import server


class DecisionTestCase(unittest.TestCase):
    def setUp(self):
        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

    def test_server(self):
        self.assertEquals((self.client.get('/')).status_code, 200)
        self.assertEquals((self.client.get('/decisions')).status_code, 405)
        self.assertEquals((self.client.get('/doesnotexist')).status_code, 404)

    def test_change_name_returns_successful_response(self):
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

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.headers.get('content-type'), 'application/json')

    def test_change_name_returns_bad_request(self):
        data = {
            "action": "change-name-marriage",
            "context": {
                "session-id": "123456",
                "transaction-id": "ABCDEFG"
            }
        }

        rv = self.client.post('/decisions',
                              data=json.dumps(data),
                              content_type='application/json')

        self.assertEquals(rv.status_code, 400)
        self.assertEquals(rv.headers.get('content-type'), 'application/json')
