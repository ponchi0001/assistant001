#coding:UTF-8
import requests
import json

#毎日22時の通知を行うスクリプト。
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#宛先はアシスタント
    token = "DE2O0rewCeKShOPQ4jZBPhZE1dW9naQvZw9ufsz5nYv"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
    path = '/home/pi/work/table/mTABLE2200'
    with open(path) as f:
        mo = f.readlines()
    #宛先はアシスタント
    msg = ""
    for mm in mo:
        msg = msg + mm
    #print(msg)
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
