# transport mode selection

distance=int(input("Enter distance in km: "))

if distance<3:
  print("walk")
elif distance<15:
  print("Bike")
else:
  print("Car")
  