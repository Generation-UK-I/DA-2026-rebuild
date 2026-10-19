import # import required libraries
import # import required libraries

url = # Add URL
params = {
    "latitude": # Find the correct latitude...
    "longitude": # and longitude with Google Maps
    # Add additional parameters here
}

response = requests.get( , params=params) # Complete the get() method to create a response object
data = response.json()

print("Status code :", response.status_code) # Verify HTTP response code

hourly_temps = data["hourly"]["temperature_2m"]
print(f"\nHourly readings: {len(hourly_temps)}")
print(f"Average hourly temperature: {sum( ) / len( ):.1f}") # Complete this calculation for average hourly temps

# Use hourly_temps block as a basis for calculating average hourly_rain

daily = data[" "]
units = data[" "]
print("\nDaily forecast:")
for i in range(len(daily[" "])): # Identify correct key
    print(
        f"{daily['time'][i]}  "
        f"max {daily[' '][i]}{units[' ']}  " # Identify correct keys
        f"min {daily[' '][i]}{units[' ']}  " # Identify correct keys
    )
    
# Lookup weather code against codes dictionary - available on API docs page

print(f"Current Temperature: {data[key1][key2]}C") # Example print statement - replace placeholder values

with open(" ", " ") as file:
    json.dump( , file, indent=2) # starter code for persistence