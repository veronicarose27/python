a=int(input())
x=1
y=1
count=2
print(x,y,end=" ")
while(count<a):
    z=x+y
    print(z, end=" ")
    x=y
    y=z
    count=count+1
