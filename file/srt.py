import requests
from bs4 import BeautifulSoup
import csv

url = "https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000"
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")

tr = soup.select('tbody > tr')
with open("bitsum_coin.csv",'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr:
        print(r.select_one('.time').text.strip() + r.select_one('.trnNo').text)
        row = [r.select_one('.time').text.strip(), r.select_one('.trnNo').text] #한줄에 2개씩 넣겠다.
        csv_writer.writerow(row)