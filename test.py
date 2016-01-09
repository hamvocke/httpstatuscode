import app
import unittest

class StatusCodeTestCase(unittest.TestCase):
    def setUp(self):
        app.app.secret_key = 'test'
        self.app = app.app.test_client()

    def test_should_return_200_for_known_status_code(self):
        response = self.app.get('/404')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"404" in response.data)
        self.assertTrue(b"Not Found" in response.data)

    def test_should_return_404_for_unknown_status_code(self):
        response = self.app.get('/800')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b"Sorry, I couldn't find that statuscode" in response.data)

    def test_should_return_landing_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Find out what your HTTP statuscode stands for' in response.data)

    def test_should_redirect_to_existing_page(self):
        response = self.search_without_redirect("415")
        self.assertEqual(response.status_code, 302)

    def test_should_find_existing_page(self):
        response = self.search("415")
        self.assertEqual(response.status_code, 200)

    def test_should_redirect_if_searched_page_cannot_be_found(self):
        response = self.search_without_redirect("499")
        self.assertEqual(response.status_code, 302)

    def test_should_redirect_to_index_if_searched_page_cannot_be_found(self):
        response = self.search("499")
        self.assertEqual(response.status_code, 200)
        
    def search_without_redirect(self, query):
        return self.app.post('/search', data=dict(query=query), follow_redirects=False)

    def search(self, query):
        return self.app.post('/search', data=dict(query=query), follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
