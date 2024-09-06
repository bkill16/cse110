def calculate_wind_chill(temperature):
    for wind_speed in range(5, 61, 5):
        wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

def convert_celsius(temperature):
    fahrenheit = temperature * (9 / 5) + 32
    return fahrenheit

user_temperature = float(input("\nWhat is the temperature? "))
user_degree_type = input("Fahrenheit or Celsius (F/C)? ")

if user_degree_type.lower() == "c":
    converted_temp = convert_celsius(user_temperature)
    calculate_wind_chill(converted_temp)

else:
    calculate_wind_chill(user_temperature)

print()