# 최소한으로 이동할 때 거쳐간 칸의 수를 구하는 프로그램
# n x m 표에서 (1,1) 부터 (n,m)까지 이동
# 각 칸에서 1의 값이 주어진 칸 위로만 움직임 가능 

import sys
from collections import deque

# n과 m 입력 받기
n, m = map(int, input().split())
G = []

# n개의 줄을 읽어들여서 그래프에 저장
for i in range(n):
    row = list(map(int, input().split()))
    G.append(row)

def bfs(start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    que = deque([(start[0], start[1], 1)])  # (x, y, 경로 길이)
    visited = [[False] * m for _ in range(n)]  # 2D 방문 체크
    visited[start[0]][start[1]] = True

    while que:
        x, y, length = que.popleft()  # 큐에서 정점 꺼내기 
        if x == n - 1 and y == m - 1:
            return length  # 도착하면 거쳐간 칸 수 반환
        
        for dx, dy in directions:  # 현재 정점에 연결된 모든 정점 탐색
            nx, ny = x + dx, y + dy
            # 범위에 속해있고 해당 칸이 1이며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and G[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, length + 1))

    return -1  # 도착할 수 없는 경우

# BFS 실행
result = bfs((0, 0))  # (1, 1) 대신 (0, 0)으로 시작
print(result)