from django.test import Client, TestCase
from unittest.mock import patch
from .views import index

class SimpleTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('requests.get')
    def test_mocked_test_case_should_succeed(self, mock_request):
        """
        This is a simple testcase using mock feature.
        1 - Decorate the method with path (app_path.views.module).
        2 - Reference the mock in test method as param (mock_test).
        3 - Define a value of the return of method (sub method or property) to mock.
        4 - Call the mocked method and compare.
        """
        mock_request.return_value = '{origin: "177.185.2.138"}'
        response = self.client.get('/index/')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{origin: "177.185.2.138"}')