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
    
    # Store data as dictionary
    weather_data.append({
        'day': day,
        'temperature': temp,
        'condition': condition
    })
    
    # Extract temperature value (remove °C) for calculations
    temp_value = int(temp.replace('°C', ''))
    temperatures.append(temp_value)
    
    # Print each day's forecast
    print(f"{day}: {temp}, {condition}")

# Find day with highest temperature
max_temp = max(temperatures)
max_temp_days = [w['day'] for w in weather_data 
                if int(w['temperature'].replace('°C', '')) == max_temp]

# Find sunny days
sunny_days = [w['day'] for w in weather_data if w['condition'] == 'Sunny']

# Calculate average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Print results
print("\nAnalysis:")
print("-" * 30)
print(f"Highest temperature ({max_temp}°C) on: {', '.join(max_temp_days)}")
print(f"Sunny days: {', '.join(sunny_days)}")
print(f"Average temperature: {avg_temp:.1f}°C")