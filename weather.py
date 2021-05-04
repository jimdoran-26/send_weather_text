import requests, json
import os
from temp_convert import *
def get_weather(city):
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   CITY = city
   API_KEY = os.environ['api_key']
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   #print(URL)

   response = requests.get(URL)
   if response.status_code == 200:
      data = response.json()

      main = data['main']
      temperature = main['temp']
      min_temperature = main['temp_min']
      max_temperature = main['temp_max']


      temperature = kelvin_to_faren(temperature)
      min_temperature = kelvin_to_faren(min_temperature)
      max_temperature = kelvin_to_faren(max_temperature)

      humidity = main['humidity']
      pressure = main['pressure']
      report = data['weather']


      print(f"{CITY:-^30}")
      print(f"Current Temperature: {temperature}")
      print(f"Minimum Temperature: {min_temperature}")
      print(f"Maximum Temperature: {max_temperature}")

      #print(f"Humidity: {humidity}")
      #print(f"Pressure: {pressure}")
      print (f"Weather Report: {report[0]['description']}")


      return (f"{CITY:-^30}"+'\n'+f"Current Temperature: {temperature}"+'\n'+f"Minimum Temperature: {min_temperature}"+'\n'+f"Maximum Temperature: {max_temperature}"+'\n'+f"Weather Report: {report[0]['description']}")
   else:
      # showing the error message
      print("Error in the HTTP request")
