import urllib3
import json
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
print("Today=",today)

nip = "5272538934" #nip
url = f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={today}"
print(url)
try:
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    response = r.data.decode("utf-8")
    company = json.loads(response)
    print(company["result"]["subject"]["name"])
    print(company["result"]["subject"]["statusVat"])
    print(company["result"]["subject"]["accountNumbers"])
except Exception as exc:
    print("response code=",r.status)
    print(response)


