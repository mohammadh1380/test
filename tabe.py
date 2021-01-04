import stddraw
import math

#get count sample from user

n=int(input('enter your number:'))

#creat list x,y

x,y=[],[]
for i in range(n+1):
    x+=[math.pi*i/n]
    y+=[math.sin(4*x[i])+math.sin(20*x[i])]

#change size page

stddraw.setXscale(0,math.pi)
stddraw.setYscale(-2.0,2.0)

#draw chart

for i in range(n):
    stddraw.line(x[i],y[i],x[i+1],y[i+1])

stddraw.show()
