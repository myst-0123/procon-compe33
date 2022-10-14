import sys
import urllib.request

args = sys.argv

add_str = args[1]   #通信する相手側のipアドレスを指定する

# URL,保存するファイルのパスを指定
url = "http://" + add_str + ":8080/problem.wav" # URLを指定
url2 = "http://" + add_str + ":8080/problem_data.json"
save_name = "/home/procon-compe33/sound-data/problem.wav" #保存したい相対パスを指定
save_name2 = "/home/procon-compe33/problem-data.json"

# ダウンロードを実行
urllib.request.urlretrieve(url, save_name)
urllib.request.urlretrieve(url2, save_name2)
