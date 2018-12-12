import requests 

api_key = '65ad908a09ed4199c6535930504b94a149a8b544fe09dead4b636a5700723fdb'
url = "https://allsportsapi.com/api/basketball/?met=Livescore&APIkey=" + api_key
r = requests.get(url)
print(r.json())
#print(data)