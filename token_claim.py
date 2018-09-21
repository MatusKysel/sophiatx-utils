import json
from websocket import create_connection

ws = create_connection("ws://127.0.0.1:9195/")
genesis = json.load(open("genesis.json", "r"))
default_pk = "SPH1111111111111111111111111111111114T1Anm"

def get_account_history_rpc(account, start, count):
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "get_account_history", "params":[str(account), start, count], "id": 0 }))
	return json.loads(ws.recv())["result"]

def transfer(from_, to, amount, private_key):
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "transfer", "params":[from_, to, str(amount) + " SPHTX", ""], "id": 0 }))
	send_and_sign(json.loads(ws.recv())["result"], private_key)

def send_and_sign(ops, private_key):
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "send_and_sign_operation", "params":[ops, private_key], "id": 0 }))
	print(ws.recv())

def generate_key_pair():
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "generate_key_pair", "params":[], "id": 0 }))
	return json.loads(ws.recv())["result"]		

def check_in_genesis(name):
	for account in genesis:
		if(account["name"] == name):
			return True
	return False

def get_balance(account):
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "get_account_balance", "params":[str(account)], "id": 0 }))
	return round(float(json.loads(ws.recv())["result"]) / 1000000, 6) 

def key_check(account):
	ws.send(json.dumps({"jsonrpc": "2.0", "method": "get_active_authority", "params":[str(account)], "id": 0 }))
	return json.loads(ws.recv())["result"]["key_auths"][0][0]

def get_account_history(account, ops = ''):	
	max_num = get_account_history_rpc(account, -1, 1)[0][0]
	for i in range(1000, max_num + 1001, 1001):
		result = get_account_history_rpc(account, i, 1000)
		for tx in result:
			if ops != '':
			 	if(tx[1]["op"][0] == ops):
			 		print(tx[1])
			else: 		
				print(tx[1])

def token_swap_state():
	count = 0
	total = 0
	data = []
	for account in genesis:
		if(key_check(account["name"]) == default_pk):
			data = (account["name"], )
			total = total + get_balance(account["name"])
			count = count + 1

	print(total)
	print(count)

def print_top_non_swaped(num = 50):
	data = [('test', 0)]
	for account in genesis:
		if(key_check(account["name"]) == default_pk):
			data.append((account["name"], get_balance(account["name"])))

	data.sort(key=lambda tup: tup[1], reverse=True)

	print(data[:num])

def generate_key_for_acc(input, output, output_w_pk):
	input = open(input, "r")
	output = open(output, "w")
	output1 = open(output_w_pk, "w")
	for account in input:
		if(check_in_genesis(account[:20])):
			keys = generate_key_pair()
			output.write(account[:20] + " " + keys["pub_key"] +"\n")
			output1.write(account[:20] + " " + keys["pub_key"] + " " + keys["wif_priv_key"]+"\n")

def transfer_from_accounts(from_file, to):
	output1 = open(from_file, "r")
	total = 0
	for account in output1:
		params = account.split()
		amount = round(get_balance(params[0]) - float(0.01), 6)
		if(amount >= 0):
			total = total + amount
			print( "account: " + params[0] + " amount: " +  str(amount))
			#transfer(params[0], to, amount, params[2])

	print(total)		


if __name__ == "__main__":
	# generate_key_for_acc("bitz.txt", "output-bitz.txt", "output-bitz1.txt")
	# transfer_from_accounts("output-bitz1.txt", "UD4UJ/F6gI3n8SxisTXMBKdhqAY")
	token_swap_state()
	# print_top_non_swaped()
	# get_account_history("abc", "transfer")
	ws.close()

