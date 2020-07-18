#  Name : Pranav Gulavani
# College : Fergusson college 

import json
import turtle
import datetime
import collections
import math

with open('data.json') as f :
    data = json.load(f)
    
# Extracting sub dictionary and sorting it
prices = data["rates"]
prices =collections.OrderedDict(sorted(prices.items()))

# Extracting x-axis value
maxCurValue = 0
for day ,value in prices.items():
    if value['INR'] > maxCurValue:
        maxCurValue = value['INR']

# Extracting y-axis value
startDate = datetime.datetime(2020,1,1) 
endDate = datetime.datetime(2020,1,31) 
daysDiff = endDate - startDate
totalDays = daysDiff.days


t =turtle.Turtle()
screen = t.getscreen()
screen.title("INR->Blue  & GBP->green compared with EUR X-> Dates & Y-> currency value")
screen.tracer(30)
screen.setworldcoordinates(0,0,maxCurValue,totalDays)
t.goto(0,0)
t.color("blue")

# plotting graph and math.log for flattening graph
for day , value in prices.items():
    day =datetime.datetime.strptime(day,'%Y-%m-%d')
    if day>=startDate and day<=endDate:
        daysDiff=day - startDate
        totalDay =daysDiff.days
        print(value['INR'])
        t.goto(totalDay,math.log(value['INR']))

t.color("white")
t.goto(0,0)
for day , value in prices.items():
    day =datetime.datetime.strptime(day,'%Y-%m-%d')
    if day>=startDate and day<= endDate:
        daysDiff=day - startDate
        totalDay =daysDiff.days
        print(value['GBP'])
        t.color("green")
        t.goto(totalDay,math.log(value['GBP']))

screen.update()
screen.exitonclick()   
    

    
    
         
        



