#coding:UTF-8
import requests
import json
import datetime

#mobileDotimaの時間を通知する
def main(msg):
    url = "https://notify-api.line.me/api/notify"
    #ファイルを読み込んでアシスタント決定
    path = '/home/pi/work/table/sTABLE'
    with open(path) as f:
        to = f.readlines()
    #宛先はアシスタント
    token = to[0].rstrip()
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
#print("15分以内にモバイルDotimaの開始ボタンを押してください。")
    path = '/home/pi/work/table/mTABLE'
    with open(path) as f:
        mo = f.readlines()
#宛先はアシスタント
    msg = mo[0].rstrip()
#print(msg)
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
