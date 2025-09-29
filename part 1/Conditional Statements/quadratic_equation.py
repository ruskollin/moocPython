from math import sqrt

x = float(input("Value of a: "))
y = float(input("Value of b: "))
z = float(input("Value of c: "))

# quadratic equation: ax2+bx+c=0
# discriminant: b2−4ac

discriminant = y**2 - 4*x*z

root1 = (-y + sqrt(discriminant)) / (2*x)
root2 = (-y - sqrt(discriminant)) / (2*x)

print(f"\nThe roots are {root1} and {root2}")