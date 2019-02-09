#coding:UTF-8
import requests
import json

#毎月25日に家族アシスタントに送るスクリプト
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#宛先は家族アシスタント
    token = "HmRFH319MLcN6WLTY1wpeCw4Q5kSQ1YOhER4dJNcbRb"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

#メッセージを作る
    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
#メッセージの内容
def getapi():
    msg = '\n' + "今日は25日です。"+'\n' \
    + "会社への振込を忘れずにしましょう。"
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
