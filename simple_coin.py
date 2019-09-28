import math
import random
b=0
s=0
r=1000000
for i in range(r):
     a=random.randint(1,10)
     if a>5:
         s=s+1
     elif a<=5:
         b=b+1

sr=float(s/r*100)
br=float(b/r*100)
br=round(br,5)
sr=round(sr,5)
print("head = ",sr,"tail = ",br)
