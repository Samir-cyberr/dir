import requests

def get_weather_data(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Xato: {e}")
        return None

def main():
    API_KEY = "0fa7c59d745a3c26604926a4a2f1e34d"
    CITY_NAME = "Tashkent"
    
    weather_data = get_weather_data(API_KEY, CITY_NAME)
    
    if weather_data:
        print(f"Ob-havo ma'lumotlari: {weather_data}")
    else:
        print("Ob-havo ma'lumotlarini olish muvaffaqiyatsiz tugadi")

if __name__ == "__main__":
    main()