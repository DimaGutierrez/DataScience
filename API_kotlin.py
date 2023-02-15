import requests
import json

url = "https://api.example.com/data"
response = requests.get(url)
data = json.loads(response.text)
print(data)
