import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")
#tbody = soup.select_one('tbody')
#tr = tbody.select('tr')
tr = soup.select('tbody > tr')
for r in tr:
    print(r.select_one('.tit').text.strip()) #text는 문자열을 뽑아온것 
    # strip 함수는 문자열 왼쪽과 오른쪽을 날려주는 함수
    print(r.select_one('.sale').text) #.이 클래스임