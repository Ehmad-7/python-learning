class Car:
  total_cars=0
  def __init__(self,brand,model):
    self.__brand=brand
    self.__model=model 
    Car.total_cars+=1
    
  def get_brand(self):
    return self.__brand 
    
  def full_name(self):
    return f"{self.__brand} {self.__model}"
  def fuel_type(self):
    return "petrol or diesel"
  @staticmethod
  def general_description():
    return "Cars are means of transport"
  
  @property
  def model(self):
    return self.__model
  
class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battey_size=battery_size
    
  def fuel_type(self):
    return "Charging"


my_tesla=ElectricCar("Tesla",'Model S','85kwh')
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

corolla=Car("Toyota",'Corolla')
print(corolla.fuel_type())
print(corolla.model)
print(Car.general_description())
print(Car.total_cars)

myCar=Car("Ford","Mustang")
my_new_car=Car("Hyundai",'sonata')

print(myCar.brand) 
print(myCar.model)
print(myCar.full_name())

print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())

class Battery:
  def battery_info(self):
    return "THis is battery"

class Engine:
  def engine_info(self):
    return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
  pass

my_new_tesla=ElectricCarTwo('Tesla','Model X')
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())