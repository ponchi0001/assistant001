#coding:UTF-8
import requests
import json

#朝の7時半に天気予報の概要をLINEするためのスクリプト
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#宛先はアシスタント
    token = "DE2O0rewCeKShOPQ4jZBPhZE1dW9naQvZw9ufsz5nYv"#ここにアクセストークンを入力します。
    #token = "HmRFH319MLcN6WLTY1wpeCw4Q5kSQ1YOhER4dJNcbRb"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
    # APIのひな型 --- (※3)
    api = "http://weather.livedoor.com/forecast/webservice/json/v1?city={citycode}"
    #APIリクエスト
    # Weather情報を取得する
    # livedoorのAPiを利用するように改修する。
    # URL"http://weather.livedoor.com/forecast/webservice/json/v1"
    # 東京の１次細分区分は130010
    tokyo = "130010"
    # APIのURLを得る
    url = api.format(citycode=tokyo)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする --- (※7)
    data = json.loads(r.text)
    msg = (data["description"]["text"])
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
