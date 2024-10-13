import requests
from bs4 import BeautifulSoup
import smtplib

#choose your location from weather.com
page = requests.get("https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR")
soup = BeautifulSoup(page.content, 'html.parser')

class Hourly_Rain:
    def __init__(self,html_content):
        self.html_content = html_content
    
    def get_rain(self):
        temp = self.html_content.split()
        return temp[-1][-2]

def get_todays_rain():
    rain_list = []
    todays_weather = soup.find('div', class_="TodayWeatherCard--TableWrapper--wt2ea")
    li_elements = todays_weather.find_all('li')
    for li in li_elements:
        weather = Hourly_Weather(li.text)
        if weather.get_rain() != '-':
            rain_list.append(weather.get_rain())
    if max(rain_list) > 60:
        send_gmail()
      
def send_gmail():
    gmail_user = "@your_email.com"
    receiver = "@your_email.com"
    subject = "Weather Alert"
    message = "Warning: Heavy rain expected today. " 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, "your_password")
    server.sendmail(gmail_user, receiver, f"Subject: {subject}\n\n{message}")


get_todays_rain()
