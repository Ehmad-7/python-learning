file=open('test.py','w')

try:
  file.write('hello')
finally:
  file.close()
  
with open('youtube.txt','w') as file:
  file.write('hello youtube')