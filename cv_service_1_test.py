import cv_service_1
import unittest

class CvService1(unittest.TestCase):

    def setUp(self):
        self.app = cv_service_1.app.test_client()
        self.app.testing = True

    def test_healthcheck_code(self):
        response = self.app.get('/cv1/healthcheck')
        self.assertEqual(response.status_code, 200)

    def test_healthcheck_respose(self):
        response = self.app.get('/cv1/healthcheck')
        self.assertTrue("ok" in response.get_data(as_text=True))
    
    def test_helloworld_code(self):
        response = self.app.get('/cv1/helloworld')
        self.assertEqual(response.status_code, 200)

    def test_helloworld_respose(self):
        response = self.app.get('/cv1/helloworld')
        self.assertTrue("helloworld" in response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()