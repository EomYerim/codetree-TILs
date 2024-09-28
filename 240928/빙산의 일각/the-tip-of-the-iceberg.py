import sys
input = sys.stdin.readline
N=int(input())
height = [int(input()) for _ in range(N)]
dic=dict()
set_height=set(height)
for i in range(len(set_height)):
    ans=0
    h=list(set_height)[i]
    remove={h}
    flag=False
    remove_set = [i for i in height if i not in remove]
    for j in range(len(height)):
        if(height[j]-h>0):
            if(flag==False):
                ans+=1
            flag=True
        else:
            if(flag==True):
                flag=False
    dic[i]=ans
print(max(dic.values()))