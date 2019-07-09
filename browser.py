import webbrowser

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
my_keywords = ["JIAN","IU","SANA"]
for my_keyword in my_keywords:
    webbrowser.open(url + my_keyword)
