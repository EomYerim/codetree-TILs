import sys
from collections import Counter
input = sys.stdin.readline
N=int(input()) # N개의 숫자
arr=[int(input()) for _ in range(N)]
num=Counter(arr)
if(len(set(arr))==1):
    print(0)
else:
    dic=dict()
    for i in arr:
        cnt=1
        remove_set={i}
        temp = [i for i in arr if i not in remove_set]
        for j in range(1,len(temp)):
            x=temp[j-1]
            if temp[j]==x:
                cnt+=1
        dic[i]=cnt
    res= max(dic.values())
    print(res)