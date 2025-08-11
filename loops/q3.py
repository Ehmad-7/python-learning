# multiplication table

n=int(input("Enter the number: "))

for i in range(1,11):
  if(i!=5):
    print(n,'x',i,'=',n*i)