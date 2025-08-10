intro={
  "name":"Ehmad",
  "age":20,
  "role":"student",
  "address":{'street':1,'home no':3}
}

print(intro)
print(intro["name"])

print(intro["address"]['street'])

# dictionary method
print(intro.get("age"))
intro['height']="6 feet"

for x in intro:
  print(intro[x])  

print('/n')
  
for key,value in intro.items():
  print(key,value)
  
intro.pop('age')
print(intro)
intro['age']=20
print(intro)

squared_nums={x:x**2 for x in range(10)}
print(squared_nums)