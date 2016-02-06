import app
import unittest
import requests
from flask import request

class HTTPFunctionalTestCase(unittest.TestCase):

    def test_should_return_landing_page(self):
        response = requests.get('http://localhost:5000/401')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
