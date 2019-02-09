#coding:UTF-8
import requests
import json

#天気予報を毎朝7時半に伝えるスクリプト
def main(msg):
    url = "https://notify-api.line.me/api/notify"
#宛先はアシスタント
    #token = "HmRFH319MLcN6WLTY1wpeCw4Q5kSQ1YOhER4dJNcbRb"#ここにアクセストークンを入力します。
    token = "DE2O0rewCeKShOPQ4jZBPhZE1dW9naQvZw9ufsz5nYv"#ここにアクセストークンを入力します。
    headers = {"Authorization" : "Bearer "+ token}

    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
    #apikeyの指定
    apikey = "fe7069594e59d3dc30ce821c98b0f2ae"
    #天気を調べたい都市一覧
    cities = ["Tokyo,JP"]
    #APIの雛形
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
    #温度変換
    k2c = lambda k: k - 273.15
    #各都市の天気情報を取得する
    for name in cities:
        #APIのURLを得る
        url = api.format(city=name, key=apikey)
        #APIリクエストして情報を得る
        r = requests.get(url)
        #結果はJSONコードなので変換する
        data = json.loads(r.text)
        #結果をテキストで文書化
        msg1 = k2c(data["main"]["temp_min"])
        msg2 = k2c(data["main"]["temp_max"])
        msg = '\n' \
              + "都市:" + data["name"] +'\n' \
              + "天気:" + data["weather"][0]["description"] + '\n' \
              + "最高気温:" + str(msg2) + '\n' \
              + "最低気温:" + str(msg1)
        
    return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
