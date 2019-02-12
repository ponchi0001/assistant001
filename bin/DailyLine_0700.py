#coding:UTF-8
import requests
import json

#毎日朝7時の通知を行うスクリプト。
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#ファイルを読み込んでアシスタント決定
    path = '/home/pi/work/table/sTABLE'
    with open(path) as f:
        to = f.readlines()
#宛先はアシスタント
    token = to[0].rstrip()
    headers = {"Authorization" : "Bearer "+ token}
#メッセージを作る
    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
#メッセージの内容
def getapi():
    #print("15分以内にモバイルDotimaの開始ボタンを押してください。")
    path = '/home/pi/work/table/mTABLE0700'
    with open(path) as f:
        mo = f.readlines()
    #宛先はアシスタント
    msg = mo[0].rstrip()
    #print(msg)
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
