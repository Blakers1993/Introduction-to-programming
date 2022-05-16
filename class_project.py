

from ast import Try
import requests


response = requests.get("https://home.openweathermap.org/api_keys#:~:text=19a7eba0c25be07eb249f6079550c56b")
print(response.status_code)
try:
 print(response.json())
except:
    print('woops')



#opener
print('Type the city or zip of the area you need weather information for.')
city = input('city: ')
zip = input('zip')
try:
    if city in response:
        print('sweet')
    else:
        print('nooooo')
except:
    print('guess again')




