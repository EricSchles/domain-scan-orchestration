import requests
import json
header = {"Content-type": "application/json"}
payload = json.dumps({"domain":"whitehouse.gov"})
response = requests.get("https://domain-scan-javascript-services.app.cloud.gov",headers=header,data=payload)
import code
code.interact(local=locals())
