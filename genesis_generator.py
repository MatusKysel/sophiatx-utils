import json

#   "pub_key": "SPH7gMSDzNEHTJRZaeEPVN2K8tk8h2zSGNohcse1yVAVdsVTTPY8d",
#   "wif_priv_key": "5Jn1fv5RnPUFnM71CMxbiWHuWKwMDba8k6yJzByWk9MKxmaXhmD"
num_accounts = 50000
file_name = "test_gen.json"
initial_tokens = 100000000
initial_accounts = []	
for i in range(0, num_accounts):	
	account = {}
	account["name"] = "acc" + str(i)
	account["key"] = "SPH7gMSDzNEHTJRZaeEPVN2K8tk8h2zSGNohcse1yVAVdsVTTPY8d"
	account["balance"] = initial_tokens
	initial_accounts.append(account)

json_data = {}
json_data["initial_public_key"] = "SPH8MYLsv8yDKnrysHHDvXGqypG4piPx29xBapt9RXZyMGaYWESe5"
json_data["initial_balace"] = 350000000000000 - num_accounts * initial_tokens
json_data["initial_accounts"] = initial_accounts
json_data["genesis_time"] = "2018-07-17T11:00:00"
json_data["initial_chain_id"] = ""
output = json.dumps(json_data)

file = open(file_name, "w")
file.write(output)
file.close