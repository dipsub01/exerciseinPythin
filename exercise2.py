# fruits = ["apple", "banana", "cherry"]
# for iteams in fruits:
#   print(iteams)


# dip = 20
# for num in range (0,dip+1 ,2):
#     print (num)

class Vehicle:
    def __init__(self, name, license_plate, color, fuel_type):
        self._name = name
        self._license_plate = license_plate
        self._color = color
        self._fuel_type = fuel_type
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_license_plate(self):
        return self._license_plate
    
    def set_license_plate(self, license_plate):
        self._license_plate = license_plate
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    def get_fuel_type(self):
        return self._fuel_type
    
    def set_fuel_type(self, fuel_type):
        self._fuel_type = fuel_type


car = Vehicle("Toyota Camry", "ABC123", "Red", "Petrol")
print("Vehicle Name:", car.get_name())
print("License Plate:", car.get_license_plate())
print("Color:", car.get_color())
print("Fuel Type:", car.get_fuel_type())
