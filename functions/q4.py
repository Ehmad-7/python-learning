import math

def circle(radius):
  area=math.pi * radius**2
  circumference=2 * math.pi*radius
  return area,circumference

a,c=circle(9)
print("Area:",a)
print("Circumference:",c)