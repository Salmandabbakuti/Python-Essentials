#Learning Python
"""This is a
multiline
Comment."""
print("Hello, World!")
x = 5
y = 10
print(y)
print(10*5)
name = "John"
a = "awesome"
print("Python is " + a)
print(x + y)
#If you try to combine a string and a number, Python will give you an error
print(name)

p=int(1)
q=int(1.8)
r=float(3.8)
s=float(3)
print(p,q,r,s)
print(name.lower())
print(name.upper())
z = input("Enter Your Name: ")
print("Hello," + z)
if x==5:
    print ("X is five")
else:
    print ("X is not five")
if x!=4:
    print("X is not Four")
    print("X is greater than 3 and less than 6:", x>3 and x<6)
fruits=["Apple","Banana","Mango","Strawberry"]
fruits[1]="Grapes"
print(fruits[1])
for x in fruits:
    print(x)
    if x == "Mango":
        break

# List Comprehension
names = ["Alice", "Bob", "Amanda", "Charlie", "Angela"]
a_names = [name for name in names if name.startswith("A")]
print(a_names)  # Output: ['Alice', 'Amanda', 'Angela']

# Classes and Objects
class Car:
    def __init__(self, brand, model, year):  # Constructor (initializer)
        self.brand = brand  # Instance variable
        self.model = model
        self.year = year

    def display_info(self):  # Method
        return f"{self.year} {self.brand} {self.model}"

# Creating an object (instance) of the Car class
car1 = Car("Tesla", "Model S", 2023)

print(car1.display_info())  # Output: 2023 Tesla Model S

# Inheritance
class ElectricCar(Car):  # ElectricCar class inherits from Car class
    def __init__(self, brand, model, year, autonomy):
        super().__init__(brand, model, year)  # Call the parent class constructor
        self.autonomy = autonomy

    def display_info(self):  # Overriding the display_info method
        return f"{super().display_info()} with autonomy of {self.autonomy} km"

# Creating an object of the ElectricCar class
car2 = ElectricCar("Tesla", "Model 3", 2022, 500)

print(car2.display_info())  # Output: 2022 Tesla Model 3 with autonomy of 500 km