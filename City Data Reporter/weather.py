# Define Known Cities and Default Data
KNOWN_CITIES = {
    "New York",
    "London",
    "San Francisco", # The corrected spelling is used for look-up
    "Tokyo"
}

# Sample data for all known cities (simulating a database or API cache)
WEATHER_DATA = {
    "New York": {'temperature': 70, 'description': 'chilly rain'},
    "London": {'temperature': 50, 'description': 'overcast'},
    "San Francisco": {'temperature': 85, 'description': 'foggy and cool'},
    "Tokyo": {'temperature': 58, 'description': 'sunny and warm'}
}
# Fallback data
DEFAULT_CITY = "London"
DEFAULT_DATA = WEATHER_DATA[DEFAULT_CITY] 

# Get and Normalize User Input
raw_input = input("Enter a city name: ")

# Normalization: Trim whitespace and convert to Title-case for consistent 
# look-up
normalized_city = raw_input.strip().title()

# Validate and Select Data
city_data = {}
final_city_name = "" # Store the name used in the report

if normalized_city in KNOWN_CITIES:
    # City is recognized: use the specific data
    city_data = WEATHER_DATA[normalized_city]
    final_city_name = normalized_city
    print(f"\nWeather data found for {final_city_name}.")
else:
    # City is NOT recognized: fall back to default
    city_data = DEFAULT_DATA
    final_city_name = DEFAULT_CITY
    print(
        f"\nCity '{raw_input}' not recognized. Showing weather "
        f"for {DEFAULT_CITY} instead."
        )

# Add the final city name to the data structure
city_data['city'] = final_city_name

# Process, Print, and Write Data (similar to original assignment)
report_string = (
    f"The current weather in {city_data['city']} is "
    f"{city_data['description']} with a temperature "
    f"of {city_data['temperature']} degrees Celsius."
)
print(report_string)

with open('report.txt', 'w') as file:
    file.write(report_string)