import json
import requests

url = "http://socket1.sophiatx.com:9193"
default_pk = "SPH1111111111111111111111111111111114T1Anm"

def list_wittneses_by_vote(count = 100):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "alexandria_api.list_witnesses_by_vote", "params": {"name": "" , "limit":1000}, "id": 0 }))
	return json.loads(r.text)["result"]["witnesses_by_vote"]
	
def witness_statistics():
	witnesses = list_wittneses_by_vote()
	enabled = 0
	disabled = 0
	running_new = 0

	for witness in witnesses: 
		if(witness["signing_key"] == default_pk):
			disabled = disabled + 1
			print(witness["owner"] + ";disabled;" + str(witness["running_version"]))
		else:
			enabled = enabled + 1
			print(witness["owner"] + ";enabled;" + str(witness["running_version"]))
			if(witness["running_version"] == "1.1.0"):
				running_new = running_new + 1

	print("Number of enabled witnesess: " + str(enabled))
	print("Number of disabled witnesess: " + str(disabled))
	print("Number of witnesess running new version: " + str(running_new))


if __name__ == "__main__":
	witness_statistics()

