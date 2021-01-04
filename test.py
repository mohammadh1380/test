import stdio
import sys
import random
import stddraw
import color
stddraw.setXscale(0.0,12)
stddraw.setYscale(0.0,0.1)
moves=int(sys.argv[1])
n=stdio.readInt()
stdio.readInt()
stddraw.setPenColor(color.GREEN)
p=[[0.0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        p[i][j]=stdio.readFloat()

hits=[0]*n
page=0

for i in range(moves):
    r=random.random()
    total=0.0
    for j in range(n):
        total+=p[page][j]
        if r<total:
            page=j
            break
    hits[page]+=1
x,y=0.1,0.0
x1=0.05
for v in hits:
    stddraw.filledRectangle(x,y,x1,1.0*v/moves)
    x+=0.2
stddraw.show()
