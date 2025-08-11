# factorial

n=int(input("Enter the number: "))
factorial=1

while n>0:
  factorial=factorial*n
  n-=1
  
print("Factorial:",factorial)