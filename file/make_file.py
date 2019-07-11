# f = open("student.txt",'w') # student을 연다. w(write)라는 방식으로
# f.write("안녕하세요")
# f.close()

import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")

tr = soup.select('tbody > tr')
with open("exchange.txt",'w') as f:  # 오픈이라고 하는 열어진 함수를 이 안에서는 f로 쓰겠다, w(write 앞에서부터 덮어쓰기),r(read읽기)a(add추가)
    for r in tr:
        f.write(r.select_one('.tit').text.strip()) 
        f.write(r.select_one('.sale').text + "\n")  #줄바꿈
        
        
