import json
import requests
import random
from threading import Thread

concurrent = random.randrange(1000)

url = "http://127.0.0.1:9192" #https://socket1.sophiatx.com
sender = "initminer" #TODO
pk = "5KQMUz1SXuco49BkqYsjhWwF53kNmr4XuEvjAdszE62Cbw53Uf8" #TODO

def transfer(from_, to, amount, private_key):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "alexandria_api.transfer", "params":{"from": from_ , "to" : to, "amount" : amount, "memo" : ""}, "id": 0 }))
	send_and_sign_http(json.loads(r.text)["result"]["op"], private_key)

def send_and_sign_http(ops, private_key):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "alexandria_api.send_and_sign_operation", "params":{"op": ops, "pk" : private_key}, "id": 0 }))
	print(r.text)

def paralel_trans():
	transfer(sender, sender, "1 SPHTX", pk)
	
if __name__ == "__main__":
	for i in range(concurrent):
	    t = Thread(target=paralel_trans)
	    t.daemon = True
	    t.start()
