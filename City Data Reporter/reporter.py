
import requests
import json
import csv


class WeatherReporter:
    """Class for weather reporting."""
    
    def __init__(self):
        """Initialize the weather reporter."""
        self.api_key = "69fee4e998523dd15ee0205fdbf1868d"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.csv_filename = "city_data.csv"
        
    def get_city_input(self):
        """
        Get and validate city name input from user.
        """
        while True:
            city = input("Enter a city name: ").strip()
            if city:
                return city
            else:
                print("Error: City name cannot be empty. Please try again.")
    
    def get_weather_data(self, city):
        """
        Retrieve weather data from OpenWeatherMap API.
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Get temperature in Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status() # Raises an HTTPError for bad responses
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            return None
    
    def parse_weather_data(self, data):
        """
        Parse and extract relevant weather information from API response.
        """
        try:
            weather_info = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
            return weather_info
        except KeyError as e:
            print(f"Error parsing weather data: Missing key {e}")
            return None
    
    def display_weather_summary(self, weather_info):
        """
        Display formatted weather summary to console.
        """
        print("\n" + "="*50)
        print("WEATHER REPORT")
        print("="*50)
        print(f"City: {weather_info['city']}")
        print(f"Country: {weather_info['country']}")
        print(f"Temperature: {weather_info['temperature']:.1f}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Description: {weather_info['description'].title()}")
        print("="*50)
    
    def write_to_csv(self, weather_info):
        """
        Write weather data to CSV file with proper headers.
        """
        # Check if file exists by trying to read it
        file_exists = True
        try:
            with open(
                self.csv_filename, 
                'r', 
                newline='', 
                encoding='utf-8'
            ) as csvfile:
                pass  # File exists
        except FileNotFoundError:
            file_exists = False
        
        with open(
            self.csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'City', 'Country', 
                'Temperature (C)', 'Humidity (%)', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header if file is new
            if not file_exists:
                writer.writeheader()
            
            # Write weather data
            writer.writerow({
                'City': weather_info['city'],
                'Country': weather_info['country'],
                'Temperature (C)': f"{weather_info['temperature']:.1f}",
                'Humidity (%)': weather_info['humidity'],
                'Description': weather_info['description']
            })
        
        print(f"Weather data saved to {self.csv_filename}")
    
    def read_csv_data(self):
        """
        Read weather data from CSV file.
        """
        weather_data = []
        
        try:
            with open(
                self.csv_filename, 
                'r', 
                newline='', 
                encoding='utf-8'
            )as csvfile:
                reader = csv.DictReader(csvfile)
                weather_data = list(reader)
        except FileNotFoundError:
            print(f"No data file found: {self.csv_filename}")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        
        return weather_data
    
    def report_csv_data(self):
        """
        Report on data stored in CSV file.
        """
        weather_data = self.read_csv_data()
        
        if not weather_data:
            print("No weather data available in CSV file.")
            return
        
        print(f"\nCSV Data Report:")
        print(f"Number of cities in file: {len(weather_data)}")
        print("\nCity Data:")
        print("-" * 40)
        
        for record in weather_data:
            print(f"City: {record['City']}")
            print(f"Temperature: {record['Temperature (C)']}°C")
            print(f"Humidity: {record['Humidity (%)']}%")
            print(f"Description: {record['Description']}")
            print("-" * 40)
    
    def run(self):
        """
        Program execution flow.
        """
        print("Welcome to the Weather Reporter!")
        print("This program will fetch weather data and save it to a " \
        "CSV file.")
        
        while True:
            print("\nOptions:")
            print("1. Get weather for a city")
            print("2. View stored weather data")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                # Get weather for a city
                city = self.get_city_input()
                print(f"Fetching weather data for {city}...")
                
                weather_data = self.get_weather_data(city)
                if weather_data:
                    parsed_data = self.parse_weather_data(weather_data)
                    if parsed_data:
                        self.display_weather_summary(parsed_data)
                        self.write_to_csv(parsed_data)
                    else:
                        print("Failed to parse weather data.")
                else:
                    print("Failed to retrieve weather data. Please check the "
                    "city name and try again.")
            
            elif choice == '2':
                # View stored data
                self.report_csv_data()
            
            elif choice == '3':
                print("Thank you for using the Weather Reporter!")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Function to run the weather reporter program."""
    print("Weather Reporter")
    print("=" * 30)
    print("Welcome! This program will fetch weather data and save it to a " 
    "CSV file.")
    print()
    
    # Create and run the weather reporter
    reporter = WeatherReporter()
    reporter.run()


if __name__ == "__main__":
    main()
