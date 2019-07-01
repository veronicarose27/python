N=int(input())
p,q=0,1
print(q,end=" ")
for i in range(1,N):
    s=p+q
    print(s, end=" ")
    p,q=q,s
    
