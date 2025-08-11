# Age group Categorization

age=int(input("Enter age: "))

if(age<13):
  print("Person is a Child")
elif(age>=13 and age<=19):
  print("Person is a Teenager")
elif(age>20 and age<=59):
  print("Person is an Adult")
else:
  print("Person is Senior")