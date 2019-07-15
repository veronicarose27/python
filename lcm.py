l,o=map(int,input().split())
t=[]
b=[]
lcm=1
c=max(l,o)
for i in range(1,c):
    if(l%i==0 and o%i==0):
        t.append(i)
        l=l//i
        o=o//i
b.append(l)
b.append(o)
for j in t:
    lcm=lcm*j
for k in b:
    lcm=lcm*k
print(lcm)

