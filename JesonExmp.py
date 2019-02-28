import json
with open('data.json')as f:
    data = json.load(f)
    
##print(data)
##
##
##with open('data1.json','w')as f:
##    json.dump(data,f)
##print(type(data))
##print(data)


jsonstr = json.dumps(data)
##print(jsonstr)
##print(type(jsonstr))

data = json.loads(jsonstr)
print(data["Varun"])
