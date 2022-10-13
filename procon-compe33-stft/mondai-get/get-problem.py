import json
import urllib.request
from urllib.error import URLError
from urllib.error import HTTPError

import os
from webbrowser import get

global_url = 'https://procon33-practice.kosen.work'

TOKEN = os.environ.get("TOKEN")


print(TOKEN)

def main():
	print("tinpo")
	a = get_problem()
	print(a)
	problem_wev = get_chunks(a)
	print(problem_wev)
	for i in problem_wev:
		print(i)
		get_wavfile(i)


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
		url = global_url + "/problem/chunks/:" + filename + "?token=" + TOKEN
		# headers = {
		# 	'procon-token' : TOKEN,
		# }
		urllib.request.urlretrieve(url, filename)
		return True
	except HTTPError as e:
		print('raise HTTPError')
		print(e)
		return False
	except URLError as e:
		print('raise URLError')
		print(e)
		return False



if __name__ == "__main__":
	main()