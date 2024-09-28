import sys
input = sys.stdin.readline
N=int(input())
height = [int(input()) for _ in range(N)]
dic=dict()
for i in range(len(set(height))):
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
    dic[i]=ans
print(max(dic.values()))