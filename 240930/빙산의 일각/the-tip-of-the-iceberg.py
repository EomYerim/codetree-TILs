import sys
from collections import defaultdict

input = sys.stdin.readline

def max_iceberg_chunks(N, heights):
    # 높이별로 인덱스를 저장
    height_indices = defaultdict(list)
    for i, h in enumerate(heights):
        height_indices[h].append(i)
    
    # 높이를 오름차순으로 정렬
    sorted_heights = sorted(set(heights))
    
    max_chunks = 0
    chunks = 0
    last_index = -2  # 이전 빙산의 인덱스
    
    for h in sorted_heights:
        for i in height_indices[h]:
            if i > last_index + 1:
                # 새로운 덩어리 시작
                chunks += 1
            last_index = i
        max_chunks = max(max_chunks, chunks)
    
    return max_chunks

# 입력 처리
N = int(input())
heights = [int(input()) for _ in range(N)]

# 결과 출력
print(max_iceberg_chunks(N, heights))