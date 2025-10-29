# Ask the user for width and height
#(assume they put in valid data)

width = float(input("Width :"))
height = float(input("Height"))

#caculate the area / perimeter
area = width * height
perimeter = 2 * (width+ height)

#Outpout the area and perimeter

print()
print(f"Perimeter: {perimeter}units")
print(f"Area: {area} square units")