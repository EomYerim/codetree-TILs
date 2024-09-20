import sys
input = sys.stdin.readline
N = int(input())
num = [int(input()) for _ in range(N)]
max_length = len(str(max(num)))
numbers = [str(i).zfill(max_length) for i in num]
max_count = 0 # 최대 개수 저장

for i in range(N):
    valid_set = [numbers[i]] 
    for j in range(i + 1, N):
        check = True  # valid_set에 포함될 수 있는지 여부
        for k in range(max_length):
            if int(numbers[i][k]) + int(numbers[j][k]) >= 10:
                check = False
                break
        if check:
            valid_set.append(numbers[j])
    max_count = max(max_count, len(valid_set))

print(max_count)