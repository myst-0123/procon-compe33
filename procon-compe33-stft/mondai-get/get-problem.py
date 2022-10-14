import json
import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

import os
from webbrowser import get

global_url = 'https://procon33-practice.kosen.work'
global_jsonfile = 'ファイルパス'

TOKEN = os.environ.get("TOKEN")


print(TOKEN)

def main():
	# testコード
	json_problen = get_problem()
	print(json_problen['chunks'])
	print(json_problen['id'])
	problem_wev = get_chunks(json_problen['chunks'])
	print(problem_wev)
	for i in problem_wev:
		print(i)
		get_wavfile(i)
	with open(global_jsonfile) as f:
		json_answer = json.load(f)

	anstime = post_problem(json_answer)
	print(anstime)

def get_match():
	try:
		response = urllib.request.urlopen(global_url + "/match?token=" + TOKEN)
		json_data = json.loads(response.read())
		problems = json_data["problems"]
		print(problems)
		return problems
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

		# with urllib.request.urlopen(req) as res:
		# 	html = res.read().decode("utf-8")
		# 	print(html)

		val = json_data["chunks"]
		return val
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False

def get_wavfile(filename):
	try:
		url = global_url + "/problem/chunks/" + filename
		print(url)
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