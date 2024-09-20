import sys
input = sys.stdin.readline
N = int(input())
num = [int(input()) for _ in range(N)]
max_length = len(str(max(num)))
numbers = [str(i).zfill(max_length) for i in num]

arr=[]
def trace(i):
    cnt=1
    for j in range(1,N):
        temp=int(numbers[j-1][i]) # 0
        if temp+int(numbers[j][i])<10:
            cnt+=1
    return arr.append(cnt)

        


for i in range(max_length):
    trace(i)
print(min(arr))