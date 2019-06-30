N=int(input())
arr = list(map(int, input().split()))
arr.sort()
n=len(arr)
if(n%2!=0):
    z=(n)//2
    print(arr[z])
else:
    w=arr[n//2]+arr[(n-1)//2]
    e=w/2
    print(e)
