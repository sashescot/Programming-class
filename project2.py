##########
#Sasha Escoto 
#Purpose: Calculate volume of a cylinder when user provides a radius value and a height value
#To learn more about the formula visit: Khan Academy
##########
##########
#Sample input vaules:
#Radius: 10
#Height: 10
#Expected output: 3141.59

#Radius: 24
#Height: 40
#Expected output: 72382.29
##########

import math #math package

#user message prompt 
print("This calculator finds the volume of a cylinder")

#input prompt for radius value
radius_text = float(input('Please provide a radius value:\n'))

#input prompt for height value
height_text = float(input('Please provide a height value:\n'))

#Calculations of volume formula for a cylinder
#math package: math.pi
#pow(): radius exponent
volume =  math.pi * pow(radius_text, 2) * height_text

#round result to 2 decimal places
result = round(volume, 2)

#Output
print ("The volume of the cylinder is: " + str(result))
