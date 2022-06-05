
#let's import everything we will need for this program to function
from ast import Try
from pydoc import visiblename
from socket import fromfd
import requests
import argparse
import json
from configparser import ConfigParser
from urllib import parse, request


#this will be the constant for our API source
api_url = "http://api.openweathermap.org/data/2.5/weather"

#all information will be pulled from the API stored in the ini file 
def api_key(): 
    config = configparser()
    config.read('secrets.ini')
    return config['openweather']['api_key']

#opener
print('Type the city of the area you need weather information for.')
city = input('city: ')



if city == '__main__':
 print(api_key(city.json))












#helps process user input
def read_input(city):
    parser = argparse.ArgumentParser()
    parser.add_argument('city', nargs="+", type=str)
    
    return parser.parse_args()
if city == "__main__":
    user_args = read_input()
    print(user_args.city)
print(read_input(city).json)  



try:
    api_key.status_code
except:
    print('woops')







#formatting for weather information to user
def weathers():
    
    print(name)
    print(visibility) 
    print(clouds)
    print(temp)
    print(feels_like)
    print(temp_min)
    print(temp_max)
    print(pressure)
    print(humidity)

#sets up our input to pull information
def query():
    url_encoded_city_name = parse.quote_plus('city')
    url = (
        f"{api_url}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key()}")
    return url
def format_weather(weathers):
    response = request.urlopen(query)
    data = response.read()
    return json.loads(data)
print(format_weather(city))
try:
    if city in api_key():
        print('Correct data input')
    else:
        print('nooooo')
except:
    print('guess again')




