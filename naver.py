import requests
from bs4 import BeautifulSoup

response = requests.get("http://naver.com").text
soup = BeautifulSoup(response,"html.parser")
naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")

print(naver.text)
