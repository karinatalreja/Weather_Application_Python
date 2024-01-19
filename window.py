from tkinter import *
import requests
import json
from datetime import datetime

#TKINTER WINDOW INITIALIZATION
root = Tk()
root.geometry('400x600')
root.resizable(0,0)
root.title("Weather Application")
#DONE

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def close_window():
    root.destroy()

city_value = StringVar()

def showWeather():
    api_key = "d0da52e9ebd1ddfe1a506c87a9200abb"
    
    city_name = city_value.get()
    
    weather_info = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ city_name + "&appid="+api_key).json()
       
    tfield.delete("1.0","end")
    
    if weather_info['cod'] == 200:
        kelvin = 273 
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\n\nTemperature (Celsius): {temp}°\n\nFeels like in (Celsius): {feels_like_temp}°\n\nPressure: {pressure} hPa\n\nHumidity: {humidity}%\n\nSunrise at: {sunrise_time}\n\nSunset at: {sunset_time}\n\nCloud: {cloudy}%\n\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    tfield.insert(INSERT, weather) 

city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) 
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=20)
tfield.pack()
Button(root, command = close_window, text = "EXIT", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 10)
root.mainloop()

    
