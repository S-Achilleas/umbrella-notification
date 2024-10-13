import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR")
soup = BeautifulSoup(page.content, 'html.parser')

todays_weather = soup.find_all('div', class_='"TodayWeatherCard--TableWrapper--wt2ea"')