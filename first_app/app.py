from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")                          # route 는 경로를 받아주는 것 , / : 최상단을 의미한다. 서버의 루트 주소를 의미
def hello():                             # hello함수 정의
    return "Hello World!"                # 결과 Hello World 

@app.route("/hi")                        
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")                 
def html_tag():
    return "<h1>안녕하세요</h1>"          # 안녕하세요 출력

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1>
    <h2>반갑습니다</h2>
    """

import datetime
@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    endday = datetime.datetime(2019,11,29)
    d = endday-today
    return f"1학기 종료까지{d.days}일 남음!!" #string으로 변환

@app.route("/html_file")
def html_file():
    return render_template('index.html')

@app.route("/greeting/<string:name>") #string 이라는 변수이름을 name으로 지정한것
def greeting(name):                   #데이터를 함수에 넣는다.
    return f"안녕하세요{name}님!!"

@app.route("/cube/<int:num>")       #num을 int로 받음
def cube(num):                      #num을 함수로 넣음
    a = num**3                      #num**3을 a에 넣음
    return f"{num}의 세제곱은{a}"    #f로 출력

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)


@app.route('/greeting_html/<string:name>')
def greeting_html(name):
    return render_template("greeting.html", name=name)

import random
@app.route("/lunch")
def lunch():
    menu = {
        "짜장면" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDwCVx1BzwRDkn4Ru-C4WVxB7D42OPLqVxotnrs8vywFHZRmEK",
        "짬뽕" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSezu9IiSd-pAEFpvbBTqZ8nQVncMwRV8oIz2xuxpqRO4d7PRVL",
        "볶음밥" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjK-n6Ve_4mU9sw-r3BX-oQ4WlNJo3pTOpsaC75rNlQLv39WFO",    
    }

    menu_list = list(menu.keys()) # ["짜장면","짬뽕","스파케티"]
    pick = random.choice(menu_list)
    img = menu[pick] # dictionary에 있는 key 접근은 []로 한다.
    return render_template("lunch.html", pick=pick, img=img)


@app.route('/movies')
def movies():
    movies_list = ['스파이더맨', '토이스토리', '알라딘', '존윅']
    return render_template("movies.html", movie_list=movies_list)

@app.route('/ping')
def ping():
    return render_template("ping.html")

@app.route('/pong')
def pong():
    user_input = request.args.get("test")
    return render_template("pong.html", user_input=user_input)

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/text")
def text():
    return render_template("text.html")

import requests
@app.route("/result")
def result():
    raw_text = request.args.get('raw')     # args는 dictionary 요청에 의한 딕셔너리값중에서 raw만 뽑아서 raw_text에 담을꺼야
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url+raw_text).text # 리퀘스트한테 get을 시킨다.
    return render_template("result.html", res=res)

@app.route("/game")
def game():
    return render_template("game.html")

import random
@app.route("/game_r")
def game_r():
    cha = {
        "게임천재" : "https://opgg-com-image.akamaized.net/attach/images/20190226083413.642488.jpeg",
        "코딩천재" : "https://img.sbs.co.kr/newimg/news/20180601/201188704_700.jpg" ,
        "변태" : "https://i.ytimg.com/vi/Ghs6gdOVC4c/maxresdefault.jpg",
        "순진함" : "https://t1.daumcdn.net/cfile/tistory/0355B03A50AC7CCA0C",
        "게임바보" : "https://img.insight.co.kr/static/2018/09/20/700/p617yveo924u758a3k78.jpg"}
    
    cha_list = list(cha.keys()) 
    pick = random.choice(cha_list)
    img = cha[pick] 
    return render_template("game_r.html", pick=pick, img=img)

@app.route("/lotto")
def lotto():
    return render_template("lotto.html")

@app.route("/lotto_result")
def lotto_result():
    #사용자가 입력한 정보를 가져오기
    numbers = request.args.get('numbers').split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n)) 

    #user_numbers = [1,2,3,4,5,6]
    #로또 홈페이지에서 정보를 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()

    winning_numbers = [] #비어있는 리스트
    for i in range(1,7): #1이상 7미만 까지 i 를 돌린다.
        winning_numbers.append(lotto_numbers[f'drwtNo{i}']) # f스트링을 쓴다. #dowNo1~6까지의 정보를 받아와서 비어있는 리스트에 넣는다
    bonus_number = lotto_numbers['bnusNo']
    
    result = "1등"

    matched = set(user_numbers) & set(winning_numbers) # 교집합 비교하는 것

    if len(matched) == 6:
        result = "1등"
    elif len(matched) == 5:
        if bonus_number in user_numbers:        #보너스가 유저 안에 있으면 true를 반환하는 코드
            result = "2등"
        else :
            result = "3등"
    elif len(matched) == 4:
        result = "4등"
    elif len(matched) == 3:
        result = "5등"
    else :
        result = "꽝"
    

    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, b=bonus_number, r=result)

if __name__ == '__main__':
    app.run(debug=True)