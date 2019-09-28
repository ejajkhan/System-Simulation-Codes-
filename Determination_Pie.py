import random
import math
inn=0
out=0
r=100000
for i in range(r):
    r1=random.randint(1,99)
    r1=float(r1/100)
    r2=random.randint(10,99)
    r2=float(r2/100)
    x=1-(r1*r1)
    x=math.sqrt(x)
    if r2<=x:
        inn=inn+1
    elif r2>x:
        out+=1
pie=(inn/r)*4
print("\n\n pie is ",pie)
    