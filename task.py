#  Name : Pranav Gulavani
# College : Fergusson college 

import json
import turtle
import datetime


maxCurValue = 0


with open('data.json') as f :
    data = json.load(f)

prices = data["rates"]


for cost ,value in prices.items():
    if value['INR'] > maxCurValue:
        maxCurValue = value['INR']

print(maxCurValue)  
startDate = datetime.datetime(2020,1,1) 
endDate = datetime.datetime(2020,1,31) 
daysDiff = endDate - startDate
totalDays = daysDiff.days

t =turtle.Turtle()
screen = t.getscreen()
screen.title("INR compared with   EUR X->currency value & Y->Dates")
screen.tracer(50)
screen.setworldcoordinates(0,0,totalDays,maxCurValue)
t.goto(0,0)
t.color("blue")
t.fillcolor("#bccee8")
t.begin_fill()


for date,value in prices.items():
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    dateDiff = date - startDate
    price = value['INR']      
    t.goto(value['INR'],dateDiff.days) 

     

t.goto(maxCurValue,0)
t.goto(0,0)
t.end_fill()    
screen.update()
screen.exitonclick()    
    

    
    
         
        
