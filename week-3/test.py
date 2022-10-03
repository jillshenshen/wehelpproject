import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json

import urllib.request as request
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
     data=json.load(response)

clist=data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
     for spot in clist:
          year = spot["xpostDate"][3]
          if year >= "5":
               file.write(spot["stitle"]+",")
               file.write(spot["address"][5:8]+",")
               file.write(spot["latitude"]+",")
               file.write(spot["longitude"]+",")
               files=spot["file"]
               url=files.split("https://")
               link="http://"+url[1]
               file.write(link+"\n")
          