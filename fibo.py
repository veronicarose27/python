a=int(input())
x=1
y=1
count=2
print(x,y,end=" ")
while(count<a):
    q=x+y
    print(q, end=" ")
    x=y
    y=q
    count=count+1
