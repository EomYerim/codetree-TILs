import sys

input = sys.stdin.readline

# n 입력
N = int(input())

# height 입력
height = [int(input()) for _ in range(N)]

# simulate 함수
def simulate(curr_height):
    curr_cnt = 0
    # 맨 왼쪽은 떠있으면
    if height[0] > curr_height:
        curr_cnt += 1
    # 이후의 height를 돌면서
    for i in range(1, N):
        # 전 인덱스 값보다 클 때
        if height[i-1] <= curr_height and height[i] > curr_height:
            curr_cnt += 1
    return curr_cnt

max_cnt = 0
max_height = max(height)

# 완전 탐색 
for i in range(max_height + 1):
    max_cnt = max(max_cnt, simulate(i))

# 출력
print(max_cnt)