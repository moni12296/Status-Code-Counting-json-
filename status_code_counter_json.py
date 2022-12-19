import json
with open('api-gateway.json') as file:
  sc_list=[]
  sc_dict={}
  data=json.load(file)
  for elem in data:
    count=0
    codes=elem.get('status')
    sc_list.append(codes)
for code in sc_list:
  sc_dict[code]=sc_list.count(code)
print(sc_dict)