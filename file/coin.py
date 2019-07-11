import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")

tr = soup.select('tbody > tr')
with open("bitsum_coin.csv",'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr:
        print(r.select_one('.blind').text.strip() + r.select_one('.sort_real').text)
        row = [r.select_one('.blind').text.strip(), r.select_one('.sort_real').text] #한줄에 2개씩 넣겠다.
        csv_writer.writerow(row)