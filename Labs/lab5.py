from bs4 import BeautifulSoup
import requests

def construct_links(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.content,"html.parser")
    links = bs.find_all('a')
    
    link_tuples = [(link.get('href'), link.text) for link in links if link.get('href') is not None]
    return link_tuples



def count_missing_alt(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.content,"html.parser")
    imgs= bs.findAll("img")
    if not imgs:
        return 0
    missing_alt_count = sum(1 for img in imgs if img.get('alt') is None)
    percent_missing_alt = missing_alt_count / len(imgs)
    return percent_missing_alt


def parse_json_weather(dic):
    
    for key in dic:
        info = dic[key]
        if "main" in info:
            x = info["temp"]
            y = info["humidity"]
            return (x,y)
    return None
  


def get_weather_json(lat,lon,API_key):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    
    

    #get the weather in that location

    params = {"lat": lat,
              "lon":lon,
              "appid": API_key,
              "units":"imperial"}
    
    response = requests.get(URL,params = params)

    data = response.json()
    return data
   