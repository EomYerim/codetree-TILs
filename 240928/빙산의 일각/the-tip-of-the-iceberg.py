import sys
input = sys.stdin.readline
N=int(input())
height = [int(input()) for _ in range(N)]
res=[0]*N

for i in range(N): 
    ans=0
    h=height[i]
    flag=False
    for j in range(N):
        if(height[j]-h>0):
            if(flag==False):
                ans+=1
            flag=True
        else:
            if(flag==True):
                flag=False
    res.append(ans)
print(max(res))