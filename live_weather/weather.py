#!/usr/bin/python3
# importing requests and json
import requests, json
import argparse
import sys
import os
import subprocess

def get_weather(city_name, ret_attr):

    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    #CITY = "Chennai,IN"
    #CITY = "London,uk"
    API_KEY = "DONT FORGET TO REPLACE WITH YOUR KEY. wait for few hours after creating key."
    # upadting the URL
    URL = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=metric"
    #print(URL)
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       sys = data['sys']
       cname = data['name'] + "," + sys['country']
       
       ret_dict = {}
       ret_dict['temp'] = temperature
       ret_dict['humi'] = humidity
       ret_dict['pres'] = pressure

       print(f"{cname:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
       return ret_dict[ret_attr]
    else:
       # showing the error message
       print("Error in the HTTP request")


if __name__ == '__main__':
    # weather.py executed as script
    # usage: ./wrapper.py [options] <ip_address>
    parser =  argparse.ArgumentParser(usage = "./weather.py [-h] [-c <city,country>] ")

    # required argument

    # optional arguments
    parser.add_argument('-c', help ='city name with country', default = "London,uk")
    parser.add_argument('-r', help ='return atribute', default = "temp")
    args = parser.parse_args()

    # Assign arguments to variables if not default
    CITY = args.c
    RET = args.r

    # do something
    get_weather(CITY, RET)
