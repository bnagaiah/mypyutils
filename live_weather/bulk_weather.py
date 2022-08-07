#!/usr/bin/python3

import weather
import contextlib, io
import argparse
import collections

def getall(sorter):
    cities = ['chennai,in', 'bangalore,in', 'coimbatore,in', 'delhi,in', 'mumbai,in']
    #cities = ['Austin,us', 'Dallas,us', 'New york,us', 'Denver,us', 'Chicago,us']
    data = {}
    for city in cities:
      f = io.StringIO()
      with contextlib.redirect_stdout(f):
        sattr = weather.get_weather(city,sorter)
      output = f.getvalue()
      data[city] = [sattr,output]
      #print(output)
      #print(city, "temperature is ", sattr)

    sorted_x = sorted(data.items(), key=lambda kv: kv[1])
    sorted_dict = collections.OrderedDict(sorted_x)
    #print(sorted_dict)
    #for city in cities:
    for city in sorted_dict:
      print(data[city][0])
      print(data[city][1])

if __name__ == '__main__':
    # bulk_weather.py executed as script
    # usage: ./bulk_wrapper.py [options] <ip_address>
    parser =  argparse.ArgumentParser(usage = "./weather.py [-h] [-s <sort by attribute>] ")

    # required argument

    # optional arguments
    parser.add_argument('-s', help ='sort atribute', default = "temp")
    args = parser.parse_args()

    # Assign arguments to variables if not default
    SORT = args.s

    # do something
    getall(SORT)

