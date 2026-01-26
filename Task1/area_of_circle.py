import math

radius = int(input("Enter the radius of the circle: "))
area = math.pi * (radius**2)

print("The area of the circle is: ", area.__round__(2))