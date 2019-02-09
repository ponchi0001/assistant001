#coding:UTF-8
import requests
import json

#19時に今日のご飯を確認する
def main(msg):
    url = "https://notify-api.line.me/api/notify"
    token = "HmRFH319MLcN6WLTY1wpeCw4Q5kSQ1YOhER4dJNcbRb"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
    msg = "今日のご飯は？"
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
