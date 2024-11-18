# Assinging variables to store numbers and preform following operations
from string import capwords
from subprocess import SubprocessError
from tarfile import LENGTH_NAME

# Add
# Sub
# Mul
# Div

x = 10
y = 20
Name = "Srini"
Age = 15
Occupation = "Pvt Employee"

print("Name :", Name)
print("Age :", Age)
print("Occupation :", Occupation)
print("Addition is", x + y, sep=' : ')
print("Subtraction is", x - y, sep=' : ')
print("Multiplication is", x * y, sep=' : ')
print("Division is", x / y, sep=' : ')

# Create a variable to hold string and converting them into Upper & Lower cases
Name = "Srinivas"
print(Name)

print(len(Name))
UC = Name.upper()
LC= Name.lower()

print(UC)
print(LC)