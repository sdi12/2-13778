"""Златно сечение:
ако c=a+b и
a:b=b:c, то казваме че имаме златно сечение"""

def golden_ratio(a,b):
    r=(a+b)/a
    r="%.1f" % (r)
    r=float(r)
    t=(a+b)/b
    t="%.1f" % (t)
    t=float(t)
    z=a/b
    z="%.1f" % (z)
    z=float(z)
    u=b/a
    u="%.1f" % (u)
    u=float(u)
    if a>b:
        if r==z:
            return True
        else:
            return False
    elif b>a:
        if t==u:
            return True
        else:
            return False

n=int(input())
for i in range(1, n):
     for y in range(1, n):
         if i+y<n:
            if golden_ratio(i,y):
                print(i,y)


