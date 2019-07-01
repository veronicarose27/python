N=int(input())
p,n=0,1
print(n,end=" ")
for i in range(1,N):
    s=p+n
    print(s, end=" ")
    p,n=n,s
