# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
height = 600
width = 600
length = 600

surfaceArea = (height * width + width * length + length * height)
volume = (height * width * length)
print(surfaceArea)
print(volume)