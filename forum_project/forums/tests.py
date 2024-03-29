from django.test import TestCase,SimpleTestCase
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_about_page_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    def test_submission_page_status(self):
        response = self.client.get("/submission/")
        self.assertEqual(response.status_code, 200)
        

# Create your tests here.
