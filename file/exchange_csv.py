import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")

tr = soup.select('tbody > tr')
with open("naver_exchange.csv",'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr:
        print(r.select_one('.tit').text.strip())
        print(r.select_one('.sale').text) 
        row = [r.select_one('.tit').text.strip(), r.select_one('.sale').text] #한줄에 2개씩 넣겠다.
        csv_writer.writerow(row)