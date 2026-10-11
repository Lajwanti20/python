#Question : Take a diameter of a circle from user and calculate the area of the circle. (Area = π * r * r) where r is the radius of the circle.

diameter = float(input("Enter the diameter of the circle: "))

radius = diameter / 2
area = 3.14 * (radius ** 2)
print("The area of the circle is: " ,area)