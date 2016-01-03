import app
import unittest

class StatusCodeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_should_return_200_for_known_status_code(self):
        response = self.app.get('/404');
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"404" in response.data)
        self.assertTrue(b"Not Found" in response.data)

    def test_should_return_404_for_unknown_status_code(self):
        response = self.app.get('/800');
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b"Sorry, I couldn't find that statuscode" in response.data)

    def test_should_return_landing_page(self):
        response = self.app.get('/');
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Find out what your HTTP statuscode stands for' in response.data)

if __name__ == '__main__':
    unittest.main()
