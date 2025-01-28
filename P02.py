
import math
print('Hello! Welcome to my area calculation program!')
print('------')
print('We will begin with the area of a rectangle.\n')
wrec = float(input('What is the width of the rectangle?'))
hrec = float(input('What is the height of the rectangle?'))
arec= wrec*hrec
print('The total area for this rectangle is',arec)
print('-------')
print("Let's do a triangle now.\n")
halftri = 0.5
btri = float(input('What is the base length of the triangle?'))
htri = float(input('What is the height of the triangle?'))
atri = halftri*(btri*htri)
print('The total area of the triangle is',atri)
print('-----')
print('Lastly, lets do the area of a circle.')
pii = 3.1459
radius = float(input('All we need is the radius. Please type here:'))
A = pii * (radius * radius)
print('The total area of the circle is',A)
print('Thanks! Goodbye!')