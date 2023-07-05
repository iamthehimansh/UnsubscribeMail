import json
import webbrowser


filename=None
filename=input("Enter File name(default -> default.json): ")
if filename.strip()=="":
    filename="unsubscribe.json"
data=json.load(open(filename,"r"))
openOneByOne=input("Open One By One default y/n (f)")
if openOneByOne.lower().startswith("y"):
    openOneByOne=True;
else:
    openOneByOne=False
for i in data.keys():
    if data[i]["ischecked"]:
        webbrowser.open(data[i]["urls"][data[i]["whichChecked"]])
        if openOneByOne:
            input("If Done press Enter")
print("Congrats Unsubscribe Sucesssfully")