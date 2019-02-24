#coding:UTF-8
import requests
import json

#19時に今日のご飯を確認する
def main(msg):
    url = "https://notify-api.line.me/api/notify"
    #ファイルを読み込んでアシスタント決定
    path = '/home/pi/work/table/sTABLE2'
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
    path = '/home/pi/work/table/mTABL1800'
    with open(path) as f:
        mo = f.readlines()
    #宛先はアシスタント
    msg = ""
    for mm in mo:
        msg = msg + mm
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
