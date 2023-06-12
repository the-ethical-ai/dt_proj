import requests

# API endpoint URL
url = 'http://localhost:8000/predict'

# Send GET request
response = requests.get(url)

# Get the response JSON data
data = response.json()

# Print the response
print(data)
