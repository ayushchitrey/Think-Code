''' Q6.	Write a python program to find the volume of a sphere with diameter 12 cm'''
 #### d = diameter = 12 cm. Therefore; r = radius = d/2 = 12/2 = 6 cm
#importing libraries to get the value of pi
from math import pi
radius_of_sphere = float(input("Enter the radius of the Sphere : "))
volume_of_sphere = (4/3)*pi*(radius_of_sphere)**3
print("Volume of Sphere = ", volume_of_sphere)
                                                  