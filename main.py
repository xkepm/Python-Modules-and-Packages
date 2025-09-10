import mypackage.weather_utils as w
import mypackage.calc_utils as c
choice = input('enter c for square or f for cupe or w for weather: ')
if choice == 'c':
    n = float(input('enter a number: '))
    c.square(n)       
elif choice == 'f': 
    n = float(input('enter a number: '))
    c.cube(n)
elif choice == 'w':
    city = input("Enter city name: ")
    w.todays_weather(city)
    w.forecast(city)