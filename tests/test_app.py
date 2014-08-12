import unittest
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

        rv = self.client.post('/decisions')
        assert rv.status_code == 200
