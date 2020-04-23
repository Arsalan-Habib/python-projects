import pandas as pd
import requests
from bs4 import BeautifulSoup 
import string

URL='https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.XjbtR2gzbIU'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')

desc=week.find_all(class_='short-desc')
desc_text=[i.get_text() for i in desc]


temp=week.find_all(class_='temp')
temp_text=[i.get_text() for i in temp]


day=week.find_all(class_='period-name')
days_text=[i.get_text() for i in day]


#print(days_text,temp_text,desc_text)


weather_stuff=pd.DataFrame(

    {'Day':days_text,
    'Temperatures':temp_text,
    'short_description':desc_text
    }
)

print(weather_stuff)
weather_stuff.to_csv('weather.csv')