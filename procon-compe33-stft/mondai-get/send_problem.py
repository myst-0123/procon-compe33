import json
import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

import os
from webbrowser import get

global_url = 'https://procon33-practice.kosen.work'
global_jsonfile = './solution.json'

TOKEN = os.environ.get("TOKEN")


print(TOKEN)

def main():
	# testコード



	with open(global_jsonfile) as f:
		json_answer = json.load(f)

	anstime = post_problem(json_answer)
	print(anstime)

def create_problemjson():
	match = get_match()
	problem = get_problem()
	chunks = get_chunks(problem['chunks'])
	val = match.update(problem,**chunks)
	print(val)
	filename = "./" + "problem.json"
	os.makedirs("./"+problem["id"], exist_ok=True)
	with open(filename, mode="w") as f:
		f.write(json.dumps(problem))
	with open("./"+ problem["id"]+"/problem.json", mode="w") as f:
		f.write(json.dumps(problem))

def get_match():
	try:
		problem = get_problem()
		response = urllib.request.urlopen(global_url + "/match?token=" + TOKEN)
		json_data = json.loads(response.read())
		with open("./"+ problem["id"]+"/problem.json", mode="w") as f:
			f.write(json.dumps(problem))
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

def get_chunks(number):
	try:
		url = global_url + "/problem/chunks?n=" + str(number)
		print(url)

		headers = {
			'procon-token' : TOKEN,
		}
		deta = {}
		req = urllib.request.Request(url,deta,headers=headers)
		response = urllib.request.urlopen(req)
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