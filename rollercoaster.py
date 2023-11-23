import time

#Input
topspeed = int(input("Top speed mph: "))
minspeed = int(input("Min speed mph: "))
drop = int(input("Main drop hieght feet: "))
loop = int(input("How many loops:"))
thrill = input("do you like extreme rides: ")
grade = 0

#Middle
if thrill == "yes":
    if  topspeed > 69:
        grade += 25
    
    if minspeed > 5:
        grade += 25

    if drop > 59:
        grade += 25

    if loop > 3:
        grade += 25

if thrill == "no":
    if topspeed < 51:
        grade += 25
    
    if minspeed > 0:
        grade += 25

    if drop < 45:
        grade += 25

    if loop == 0:
        grade += 25

#Output
if grade > 74:
    print("yes this is a good coaster for you")

else:
    print("no this is not good coaster for you")
time.sleep(3)