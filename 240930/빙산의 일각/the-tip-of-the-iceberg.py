def count_connected_components(heights, water_level): # DFS를 통해 연결된 빙산의 덩어리 수 계산 
    N = len(heights)
    visited = [False] * N
    count = 0
    
    def dfs(i):
        visited[i] = True
        # 오른쪽으로 연결된 빙산 탐색
        if i + 1 < N and not visited[i + 1] and heights[i + 1] > water_level:
            dfs(i + 1)
    
    for i in range(N):
        if not visited[i] and heights[i] > water_level:
            dfs(i)
            count += 1
    
    return count

def max_iceberg_chunks(heights):
    unique_heights = sorted(set(heights))
    max_chunks = 0
    
    for water_level in unique_heights:
        chunks = count_connected_components(heights, water_level - 1)
        max_chunks = max(max_chunks, chunks)
    
    return max_chunks

# 입력 처리
N = int(input())
heights = [int(input()) for _ in range(N)]

# 결과 출력
print(max_iceberg_chunks(heights))