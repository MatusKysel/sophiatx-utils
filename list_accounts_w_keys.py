import json
import requests

url = "http://socket1.sophiatx.com:9193"
default_pk = "SPH1111111111111111111111111111111114T1Anm"
file = "accounts_w_key.txt"

def list_accounts(start, count = 1000):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "database_api.list_accounts", "params": {"start": start, "limit": count, "order":"by_id"}, "id": 0 }))
	return json.loads(r.text)["result"]["accounts"]
	
def accounts_with_key():
	output = open(file,'w') 
	start = 0
	while True:
		accounts = list_accounts(start)
		if accounts:
			if start % 1000 == 0:
				print("Writing ...", start)
			start += 1000	
			for account in accounts:
				output.write(account['name'] + ";"+ account['memo_key'] + "\n") 

		else:
			break
							                
	print("Done !")		
	output.close()	


if __name__ == "__main__":
	accounts_with_key()

