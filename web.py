import requests
from bs4 import BeautifulSoup

class Hourly_Weather:
    def __init__(self,html_content):
        self.html_content = html_content
    
    def get_rain(self):
        temp = self.html_content.split()
        return temp[-1][-2]

page = requests.get("https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR")
soup = BeautifulSoup(page.content, 'html.parser')


def get_todays_weather():
    todays_weather = soup.find('div', class_="TodayWeatherCard--TableWrapper--wt2ea")
    li_elements = todays_weather.find_all('li')
    for li in li_elements:
        weather = Hourly_Weather(li.text)
        print("Rain: ",weather.get_rain())

get_todays_weather()

'''Πρωί23°Partly Cloudy--
Απόγευμα26°Mostly CloudyRainΠιθανότητα βροχής1%
Βράδυ21°Clear NightRainΠιθανότητα βροχής2%
Νύχτα18°Clear NightRainΠιθανότητα βροχής4%'''
