import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
numbers = [int(input().strip()) for _ in range(N)]

max_length = len(str(max(numbers)))

numbers_str = [str(num).zfill(max_length) for num in numbers]

# carry가 발생하지 않는 조합인지 확인하는 함수
def is_valid_combination(num1, num2):
    for k in range(max_length):
        if int(num1[k]) + int(num2[k]) >= 10:
            return False
    return True

max_count = 1  # 최소 하나의 숫자는 항상 유효하므로 1로 초기화

# 2개 이상의 숫자 조합을 비교
for r in range(2, N + 1):  # 2개부터 N개까지 조합
    for x in combinations(numbers_str, r):
        valid = True
        for num1, num2 in combinations(x, 2):
            if not is_valid_combination(num1, num2):
                valid = False
                break
        if valid:
            max_count = max(max_count, r)

print(max_count)