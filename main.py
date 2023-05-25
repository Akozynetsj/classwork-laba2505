#1
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.e.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'htmt.parser'
    title = soup.find('title').text
    print(title)
else:
    print('немає підключення', response.status_code)