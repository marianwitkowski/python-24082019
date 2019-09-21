import urllib3
import json

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
print(url)
try:
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    response = r.data.decode("utf-8")
    data = json.loads(response)
    curr_list = data[0]["rates"]
    #print(curr_list)
    for item in curr_list:
        print(item["currency"],"=",item["mid"])
except Exception as exc:
    print("response code=",r.status)
    print(response)


