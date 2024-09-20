import sys
from itertools import combinations

input = sys.stdin.readline

# carry인지 체크
def is_carry_free(numbers):
    digit_sums = [0] * max(len(str(num)) for num in numbers)
    for num in numbers:
        for i, digit in enumerate(str(num)[::-1]):
            digit_sums[i] += int(digit)
            if digit_sums[i] >= 10: # 각 자릿수의 합이 10 이상이 되는지 체크
                return False
    return True

N = int(input())
numbers = [int(input().strip()) for _ in range(N)]

max_count = 1
for r in range(2, N + 1):
    for combo in combinations(numbers, r):
        if is_carry_free(combo):
            max_count = r
            break
    else:
        break

print(max_count)