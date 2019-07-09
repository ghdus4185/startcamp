import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(res,'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)