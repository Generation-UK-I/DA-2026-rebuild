import requests

url = # Add URL
params = {
    "latitude": # Find the correct latitude...
    "longitude": # and longitude with Google Maps
    # Add additional parameters here
}

response = requests.get() # Complete the get() method to create a response object
data = response.json()

print(f"Current Temperature: {data[key1][key2]}C") # Example print statement - replace placeholder values