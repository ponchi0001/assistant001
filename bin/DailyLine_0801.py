#coding:UTF-8
import requests
import json
import datetime

#8時に曜日毎の日課を通知するスクリプト
def main(msg):
    url = "https://notify-api.line.me/api/notify"
    #ファイルを読み込んでアシスタント決定
    path = '/home/pi/work/table/sTABLE'
    with open(path) as f:
        to = f.readlines()
    #宛先はアシスタント
    token = to[0].rstrip()
    headers = {"Authorization" : "Bearer "+ token}
    #メッセージを作成する。
    message =  msg
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです.
    r = requests.post(url ,headers = headers ,params=payload)
    
def getapi():
	aDate = datetime.date.today()
	Strweekday=["月","火","水","木","金","土","日"]
#print("今日は"+Strweekday[aDate.weekday()]+"曜日です。")
#各曜日毎のタスクを定義する。
	task=["","","","","","",""]
    path = '/home/pi/work/table/mTABLEWeektasks'

    with open(path) as f:
        mo = f.readlines()
        #	task[0]=["本気の英単語1分チャレンジ各レベル×３回"]
        #	task[1]=["本気の英単語1分チャレンジ各レベル×３回"]
        #	task[2]=["本気の英単語1分チャレンジ各レベル×３回","パジャマ交換"]
        #	task[3]=["本気の英単語1分チャレンジ各レベル×３回"]
        #	task[4]=["本気の英単語1分チャレンジ各レベル×３回"]
        #	task[5]=["パジャマ交換","爪切り"]
        #	task[6]=["スーツのアイロン掛け","眉毛の手入れ"]
    for i in range(7):
        task[i]=mo(i)

#print("今日の定型タスクは以下です。")
	msg = '\n' + \
	"今日は"+Strweekday[aDate.weekday()]+"曜日です。" + '\n' \
	 + "定型タスクは以下です。"
	for days in task[aDate.weekday()]:
	    #print("・"+days)
	    msg = msg + '\n' + "・" + days
	else:
		return msg

if __name__ == '__main__':
    msg = getapi()
    main(msg)
