import unittest
from server import calculate_income
from server import app
import requests

class TestSServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_calculate_income(self):
        input = [ 
            {"name": "Contract1", "start": 0, "duration": 5, "price": 10}, 
            {"name": "Contract2", "start": 3, "duration": 7, "price": 14}, 
            {"name": "Contract3", "start": 5, "duration": 9, "price": 8}, 
            {"name": "Contract4", "start": 5, "duration": 9, "price": 7} 
        ]

        data = {"input_payload": input}


        response = self.app.post(
                    '/spaceship/optimize/', 
                    json=data
                    )

        self.assertEqual(
            {
                'income': 18,
                'path': ['Contract1','Contract3']
            }, 
            response.json)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()