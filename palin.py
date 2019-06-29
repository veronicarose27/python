N=int(input())
rev=0
temp=N
while(N>0):
    a= N % 10
    rev= (rev*10)+a
    N=N//10
if(temp==rev):
    print('yes')
else:
    print('no')
