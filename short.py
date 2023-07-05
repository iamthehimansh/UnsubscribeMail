import json
from urllib.parse import urlparse;

data=json.load(open("data.json","r"));
newdata={}

for k in data.keys():
    newdata[k]=[];
    for i in data[k]:
        if not i in newdata[k] and bool(urlparse(i).scheme):
            newdata[k].append(i)

json.dump(newdata,open("newData.json","w"))