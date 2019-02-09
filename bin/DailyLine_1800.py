#coding:UTF-8
import requests
import json

#18時に帰宅時間を確認するLINEを送る。
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#通知先は帰宅
    token = "HmRFH319MLcN6WLTY1wpeCw4Q5kSQ1YOhER4dJNcbRb"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
    msg = "何時頃帰りますか？"
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
