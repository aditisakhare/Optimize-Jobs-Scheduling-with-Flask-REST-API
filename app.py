import requests


input_payload = [ 
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10}, 
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14}, 
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8}, 
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7} 
]

api_url = "http://127.0.0.1:8000/spaceship/optimize/"
data = {"input_payload": input_payload}
response = requests.post(api_url, json=data)
print(f"Output: {response.json()}")

