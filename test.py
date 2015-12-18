import app
import unittest

class StatusCodeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_should_return_200_for_known_status_code(self):
        response = self.app.get('/404');
        self.assertEqual(response.status, '200 OK')

    def test_should_return_404_for_unknown_status_code(self):
        response = self.app.get('/800');
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_should_return_landing_page(self):
        response = self.app.get('/');
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, b'Welcome to httpstatusco.de')

if __name__ == '__main__':
    unittest.main()
