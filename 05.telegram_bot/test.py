import requests
from decouple import config
token = config('TELEGRAM_TOKEN') #sopoo_bot
url = f"https://api.telegram.org/bot{token}/" #f 를 붙여 문자열 생성
user_id = config("CHAT_ID")

# send_url = f"{url}sendMessage?chat_id={user_id}&text=하이하이"
# requests.get(send_url)
ngrok_url = "https://ckdghdus.pythonanywhere.com"
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"
print(webhook_url)
