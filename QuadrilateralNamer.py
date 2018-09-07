#Have Fun Looking at my code, This was an Idea I had when I was bored
#This project took me a total of 1 hour and 20 mins
#Copyright Ashrith Kanakanala 2018
import math

#Introductions
print("Quadrilateral Namer")
print("By Ashrith")
print("Please enter your coords as 'x1,y1'")

#User Inputs
cord1 = str(input("Coordinate 1 = "))
cord2 = str(input("Coordinate 2 = "))
cord3 = str(input("Coordinate 3 = "))
cord4 = str(input("Coordinate 4 = "))

#Coordinate Splitter
x1,y1 = cord1.split(",")
x2,y2 = cord2.split(",")
x3,y3 = cord3.split(",")
x4,y4 = cord4.split(",")

#Integer Conversion
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
x4 = int(x4)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)
y4 = int(y4)

#Slope Formulas
try:
    slope12 = (y2 - y1)/(x2 - x1)
except ZeroDivisionError:
    slope12 = "undefined"

try:
    slope23 = (y3 - y2)/(x3 - x2)
except ZeroDivisionError:
    slope23 = "undefined"

try:
    slope34 = (y4 - y3)/(x4 - x3)
except ZeroDivisionError:
    slope34 = "undefined"

try:
    slope41 = (y1 - y4)/(x1 - x4)
except ZeroDivisionError:
    slope41 = "undefined"

#Side Lengths
dis12 = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
dis23 = ((x3 - x2) ** 2) + ((y3 - y2) ** 2)
dis34 = ((x4 - x3) ** 2) + ((y4 - y3) ** 2)
dis41 = ((x1 - x4) ** 2) + ((y1 - y4) ** 2)

dis12sqrt = math.sqrt(dis12)
dis23sqrt = math.sqrt(dis23)
dis34sqrt = math.sqrt(dis34)
dis41sqrt = math.sqrt(dis41)


#Reciprocal Function
def recip(n):
    return 1.0 / n

#Parallelogram Function
def pg():

    if slope12 == "undefined":
        negrecipslope12 = 0
    else:
        recipslope12 = recip(slope12)
        negrecipslope12 = -1 * recipslope12

    if negrecipslope12 == slope23 and dis12sqrt == dis23sqrt == dis34sqrt == dis41sqrt:
        print("Your Quadrilateral is a Square!")
    elif negrecipslope12 == slope23:
        print("Your Quadrilateral is a Rectangle!")
    elif dis12sqrt == dis23sqrt == dis34sqrt == dis41sqrt:
        print("Your Quadrilateral is a Rhombus!")
    else:
        print("Your Quadrilateral is a Parallelogram!")

#Trapezoid Functions
def tz1():
    if dis23sqrt == dis41sqrt:
        print("Your Quadrilateral is an Isoceles Trapezoid!")
    else:
        print("Your Quadrilateral is a Trapezoid!")
def tz2():
    if dis12sqrt == dis34sqrt:
        print("Your Quadrilateral is an Isoceles Trapezoid!")
    else:
        print("Your Quadrilateral is a Trapezoid!")

#Kite Function
def kite():
    print("Your Quadrilateral is a Kite!")




#Conditionals
if slope12 == slope34 and slope23 == slope41:
    pg()
elif slope12 == slope34:
    tz1()
elif slope23 == slope41:
    tz2()
elif dis12sqrt == dis23sqrt or dis34sqrt == dis41sqrt:
    kite()
else:
    print("Your Quadrilateral is just a Quadrilateral")
