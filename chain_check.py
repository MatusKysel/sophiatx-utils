import json
import requests

new_url = "http://127.0.0.1:9192"
old_url = "http://127.0.0.1:9999"
start_num = 3617000


def get_head_block(url):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "database_api.get_dynamic_global_properties", "id": 0 }))
	return json.loads(r.text)["result"]["head_block_number"]	

def get_block(url, number):
	r = requests.post(url, data = json.dumps({"jsonrpc": "2.0", "method": "block_api.get_block", "params": {"block_num": number}, "id": 0 }))
	return json.loads(r.text)["result"]
	
def chain_check():
	end_num = get_head_block(old_url)
	print(end_num)
	for x in range(start_num, end_num + 1):
		if x % 1000 == 0:
			print(x)
		try: 
			old = get_block(old_url, x)
			# new = get_block(new_url, x)
			# if not old or not new:
			# 	continue

			try: 	
				for tx in old["block"]["transaction_ids"]:
					print(tx,str(x))
			except:
				continue
		except:
			print("WTF " + str(x))				

		# print(old["block"]["transaction_ids"])
		# old = old["block"]["transaction_ids"]
		# new = new["block"]["transaction_ids"]
		# for tx in old:
		# 	if tx not in new:
		# 		print(tx + " " + str(x))


if __name__ == "__main__":
	chain_check()

