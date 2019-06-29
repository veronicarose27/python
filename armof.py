N,Q= map(int,input().split())
for a in range(N+1,Q):
    sum=0
    temp=a
    while(a>0):
        dig=a%10
        b=pow(dig,3)
        sum=sum+b
        a=a//10
    if(sum==temp):
        print(sum,end=' ')

