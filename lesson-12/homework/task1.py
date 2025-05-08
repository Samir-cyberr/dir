from bs4 import BeautifulSoup

# Parse the HTML file
with open('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the weather table
table = soup.find('table')
rows = table.find_all('tr')[1:]  # Skip header row

weather_data = []
temperatures = []

print("5-Day Weather Forecast:")
print("-" * 30)
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = cols[1].text.strip()
    condition = cols[2].text.strip()
    
    # Convert temperature to Celsius if necessary
    if '°F' in temp:
        temp_value = round((int(temp.replace('°F', '')) - 32) * 5 / 9)
    else:
        temp_value = int(temp.replace('°C', ''))

    # Store data
    weather_data.append({
        'day': day,
        'temperature': f"{temp_value}°C",  # standardize to °C
        'condition': condition
    })
    temperatures.append(temp_value)
    
    # Print forecast
    print(f"{day}: {temp}, {condition}")

# Find max temp
max_temp = max(temperatures)
max_temp_days = [w['day'] for w in weather_data if int(w['temperature'].replace('°C', '')) == max_temp]

# Sunny days
sunny_days = [w['day'] for w in weather_data if w['condition'] == 'Sunny']

# Average temp
avg_temp = sum(temperatures) / len(temperatures)

# Print analysis
print("\nAnalysis:")
print("-" * 30)
print(f"Highest temperature ({max_temp}°C) on: {', '.join(max_temp_days)}")
print(f"Sunny days: {', '.join(sunny_days)}")
print(f"Average temperature: {avg_temp:.1f}°C")
