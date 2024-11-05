# Task 1.2 : with f-string
# Expected Outpt
#  Please tell me the radius of the circle? 2
#  Area of the cirlce 12.56

radius = input("Please tell me the radius of the circle?")

print(f"Area of the cirlce {str(3.14*float(radius)**2)}")

pi = 3.14
radius = float(input("Please tell me the radius of the circle?"))
area_of_circle = pi * radius ** 2
print(f"Area of the circle {area_of_circle}")
print(f"Area of the circle {pi * radius **2 }")