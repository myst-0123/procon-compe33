from pydub import AudioSegment
import json
import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

import os
from webbrowser import get

global_url = 'http://172.28.1.1:80'
global_jsonfile = './solution.json'

TOKEN = os.environ.get("TOKEN")


print(TOKEN)

def main():
	# testコード
	# create_problemjson()
	json_problen = get_problem()
	print(json_problen['chunks'])
	print(json_problen['id'])
	problem_wev = get_chunks(json_problen)
	print(problem_wev)
	for i in problem_wev['chunks']:
		print(i)
		get_wavfile(i,json_problen['id'])
	
	print(problem_wev['chunks'])
	print(type(problem_wev['chunks']))
	sorted_problem = sorted(problem_wev['chunks'])

	sound = AudioSegment.from_file(sorted_problem[0], 'wav')
	for i in sorted_problem[1:]:
		buffer = AudioSegment.from_file(i, 'wav')
		sound = sound + buffer
	
	sound.export('../../sound-data/problem.wav', 'wav')


def create_problemjson():
	match = get_match()
	problem = get_problem()
	chunks = get_chunks(problem['chunks'])
	val = match.update(problem,**chunks)
	print(val)
	os.makedirs("./"+problem["id"], exist_ok=True)
	with open("/home//problem.json", mode="w") as f:
		f.write(json.dumps(problem))

def get_match():
	try:
		problem = get_problem()
		response = urllib.request.urlopen(global_url + "/match?token=" + TOKEN)
		json_data = json.loads(response.read())
		return json_data
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False

def get_problem():
	try:
		response = urllib.request.urlopen(global_url + "/problem?token=" + TOKEN)
		json_data = json.loads(response.read())
		with open("../../problem-data.json", mode="w") as f:
			f.write(json.dumps(json_data))
		os.makedirs("./"+json_data["id"], exist_ok=True)
		with open("./" + json_data['id'] + '/problem-data.json', mode="w") as f:
			f.write(json.dumps(json_data))
		val = json_data
		return val
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False

def get_chunks(data):
	try:
		url = global_url + "/problem/chunks?n=" + str(data['chunks'])
		print(url)

		headers = {
			'procon-token' : TOKEN,
		}
		deta = {}
		req = urllib.request.Request(url,deta,headers=headers)
		response = urllib.request.urlopen(req)
		json_data = json.loads(response.read())
		with open("./" + data['id'] + '/problem-chunks.json', mode="w") as f:
			f.write(json.dumps(json_data))
		return json_data
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False

def get_wavfile(filename,id):
	try:
		url = global_url + "/problem/chunks/" + filename
		print(url)
		save_dir = "./" + id + "/" + filename
		headers = {
			'procon-token' : TOKEN,
		}
		req = urllib.request.Request(url,headers=headers,method='GET')
		response = urllib.request.urlopen(req)
		with open(filename, mode="wb") as f:
			f.write(response.read())
		return True
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False

def post_problem(answer):
	url = global_url + "/problem"
	print(answer)
	headers = {
		'procon-token' : TOKEN,
		'Content-Type': 'application/json',
	}

	# data = {
	# 	"problem_id": id,
	# 	"answers": ["01", "02"]
	# }

	req = urllib.request.Request(url,json.dumps(answer).encode('utf-8') , headers)
	with urllib.request.urlopen(req) as res:
		body = res.read()
	json_data = json.loads(body)
	val = json_data["accepted_at"]
	return val

if __name__ == "__main__":
	main()