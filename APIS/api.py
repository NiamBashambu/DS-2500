'''
DS2500

Json data, two ways:
1. read in xx.json, printout upcoming temps
2. call API fucniton, print out upcoming temps


API KEY: ffed0167b14f7d884fae933b4c1fc551


'''

import json
import requests
FILENAME = "/Users/niambashambu/Desktop/DS 2500/APIS/forecast.json"
API_KEY = "d117fb50308d8c3422546985be308bba"
URL = "https://api.openweathermap.org/data/2.5/forecast}"

def main():
    '''
    #part one = read in JSON data from a file

    with open(FILENAME,"r") as jfile:
        data = json.load(jfile)

    #data
    #print(data)
        
    #whhat are the upcoming temps?
    for d in data["list"]:
        print(d["main"]["temp"])
        print(d["weather"][0]["description"])

'''
    #specify location?
    #parameters:lat,lon
    #make the tmps fahrenheit
    #parameter units ("units")
    lat = float(input("what latitude?\n"))
    lon = float(input("what longitude?\n"))


    #get the weather in that location

    params = {"lat": lat,
              "lon":lon,
              "appid": API_KEY,
              "units":"imperial"}
    
    response = requests.get(URL,params = params)
    data = response.json()
    print(data)
    for d in data["list"][:10]:
        print(d["main"]["temp"])
        print(d["weather"][0]["description"])


if __name__ == "__main__":
    main()