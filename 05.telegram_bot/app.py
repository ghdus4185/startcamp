from flask import Flask, request, render_template
from decouple import config
import requests
import random
from bs4 import BeautifulSoup

app = Flask(__name__)

api_url = "https://api.telegram.org"
token = config("TELEGRAM_TOKEN")
chat_id = config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config("NAVER_SECRET")

@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    msg = request.args.get('msg')
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    return render_template("send.html")

@app.route(f"/{token}", methods=['POST'])
def telegram():
    print(request.get_json())
    data = request.get_json()
    user_id = (data.get('message').get('from').get('id')) # 사용자 id 가져옴
    user_msg = (data.get('message').get('text')) # 사용자 텍스트 가져옴
    
    if data.get('message').get('photo') is None:
        if user_msg == "점심메뉴":
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            lotto_list = list(range(1,46))
            result = sorted(random.sample(lotto_list,6))
        elif user_msg[0:2]== "번역": #0부터2미만까지
            # 번역 안녕하세요 저는 누구입니다.
            raw_text = user_msg[3:] #3부터 쭉
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko",
                "target":"en",
                "text":raw_text

            }
            header = {
                'X-Naver-Client-Id' : naver_id,
                'X-Naver-Client-Secret' : naver_secret
            }
            res = requests.post(papago_url,data=data,headers=header)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            print(res.text)
            result = translate_result 
        
        elif user_msg == "뭐할까?":
            play = ["코인노래방", "LOL", "치맥", "카페", "잠자기"]
            result = random.choice(play)
        elif user_msg == "실시간검색어":
            response = requests.get("http://naver.com").text
            soup = BeautifulSoup(response,"html.parser")
            naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")
            nav = [naver]
            result = random.choice(nav)
        else:
            result = user_msg
    else:
        #사용자가 보낸 사진을 찾는 과정
        result="asdf"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = (f"{api_url}/bot{token}/getFile?file_id={file_id}")
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        print(file)

    #사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        header = {
                'X-Naver-Client-Id' : naver_id,
                'X-Naver-Client-Secret' : naver_secret
        }

        clova_res = requests.post(clova_url, headers=header, files={'image':res.raw.read()})
        
        if clova_res.json().get('info').get("faceCount"):
            # 누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이{confidence*100}%입니다."
        else:
            #사람이 없음
            result = "사람이 없습니다."

        # print(clova_res.text)

    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)

    return '', 200


if __name__ == "__main__":
    app.run(debug=True)