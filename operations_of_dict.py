data={
    "name":" Angadi Beebijan",
    "class":" B-tech",
    "Branch" :"CSE",
    "clg_name": "kishkindauniversity",
    "city_name":"Bellary",
}

print(data.keys())
print(data.values())
print(data.items())
data["id"]=10 # adding items to data
print(data)
data.pop("name")
print(data)
