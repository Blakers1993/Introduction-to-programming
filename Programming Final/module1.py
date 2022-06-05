
#let's import everything we will need for this program to function
from ast import Try
from pydoc import visiblename
from socket import fromfd
import requests
import argparse
import json
from configparser import ConfigParser
from urllib import parse, request

api_url = "http://api.openweathermap.org/data/2.5/weather"
def api_key(): 
    config = configparser()
    config.read('secrets.ini')
    return config['openweather']['api_key']
api_data = requests.get(api_key)


print(api_data.status_code)