import requests
from bs4 import BeautifulSoup
response = requests.get("https://weather.com/uk-UA/weather/today/l/Vinnytsia+Vinnytsia+Oblast?canonicalCityId=8edbdeb0bf6e909ea90ad52227b91cf736cab34f4a75e2dd89e94180b2825151")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    city = soup.fid('h1',{'class': 'CurrentConditions--locations--1YWj_'})
    if city;
    city_name = city.text.strip()
    print(city_name)
else:
    print(' місто не знайдено')



