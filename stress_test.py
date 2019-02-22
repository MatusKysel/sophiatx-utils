import json
import requests
from threading import Thread

url = "http://devnet.sophiatx.com:9193"
threads_num = 30
requests_num = 10000


def call_info():
	r = requests.post(url, data=json.dumps({"jsonrpc": "2.0", "method": "alexandria_api.info", "params": {}, "id": 0}))
	return str(json.loads(r.text)["result"])


def stress_test(prefix):
	for i in range(requests_num):
		print(prefix + ": Call-" + str(i) + ": " + call_info())


if __name__ == "__main__":
	try:
		for i in range(threads_num):
			thread = Thread(target=stress_test, args=("Thread-"+str(i),))
			thread.start()
	except:
		print("Error: unable to start thread")


