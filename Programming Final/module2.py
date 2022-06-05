from ast import Try
import requests
import json

#response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={city}&appid=19a7eba0c25be07eb249f6079550c56b')

response = requests.get("https://api.home.openweathermap.org/api_keys#:~:text=19a7eba0c25be07eb249f6079550c56b")

estab_conn = response.status_code
try:
    response.status_code
except:
    print('connection interupted')

if estab_conn == 200:
    print('connection established')

print('Type the city you need weather information for.')
city = input('city: ')

city == "name"
{name, weather}
json_response = response.city()


print(json_response)

