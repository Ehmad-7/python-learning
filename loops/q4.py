# reverse a string

string=input("Give the string: ")
reversed=''

for char in string:
  reversed=char+reversed
print(reversed)