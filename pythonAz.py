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
