import requests
import random

URL = "https://restcountries.eu/rest/v2/all"
NEW = "https://restcountries.eu/rest/v2/alpha/col"

#URL = "https://restcountries.eu/rest/v2/alpha/col"


qus = requests.get(NEW)
qus = qus.json()

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(res[0]["name"])
print("press 'enter' to continue")
input()
print(qus["name"])
