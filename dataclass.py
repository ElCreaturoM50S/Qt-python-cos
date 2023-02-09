from dataclasses import dataclass

@dataclass(order=True)
class Bike:
    brand: str
    price: int
    name: str  

my_super_bike = Bike("Składak", 9098, "Twoje Marzenie")
print(my_super_bike)