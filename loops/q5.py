# non repeated char

string=input("Give the string: ")

for char in string:
  if string.count(char)==1:
    print("Char is:",char)
    break