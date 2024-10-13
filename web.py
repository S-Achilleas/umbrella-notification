import requests
from bs4 import BeautifulSoup

class Hourly_Weather:
    def __init__(self,html_content):
        this.html_content = html_content
    
    def get_temperature(self):
        temp = self.split('°')

page = requests.get("https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR")
soup = BeautifulSoup(page.content, 'html.parser')

todays_weather = soup.find('div', class_="TodayWeatherCard--TableWrapper--wt2ea")
li_elements = soup.find_all('li',class_ =["Column--column--gUiRn Column--verticalStack--k9S2a","Column--column--gUiRn Column--active--OWlqB Column--verticalStack--k9S2a"])
counter = 0 
for li in li_elements:
    counter += 1
    if counter > 4:
        break
    print(li.text)
