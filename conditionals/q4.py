# determining if a fruit is ripe

fruit="Banana"

color=input("Give color of the fruit: ")

if fruit=="Banana":
  if color=="green":
    print("Unripe")
  elif color=="yellow":
    print("Ripe")
  elif color=="brown":
    print("OverRipe")