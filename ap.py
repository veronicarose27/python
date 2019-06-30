N,A,D=map(int,input().split())
sum=0
for i in range(0,N):
    a= A+(i*D)
    sum= sum+a
print(sum)
