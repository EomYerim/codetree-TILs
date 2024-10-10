import sys
from collections import defaultdict, deque

# 입력: n, m, s
n, m, s = map(int, input().split())
G = defaultdict(list)

# 간선 입력
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무방향 그래프인 경우 주석 해제

# 그래프의 각 정점의 리스트를 정렬
for key in G:
    G[key].sort()

def bfs(start): #start 번호 넘겨 받음 
    visited = [False] * (n + 1) # 정점 +1 만큼 리스트 크기 업데이트 
    result = []
    que = deque()
    que.append(start) 
    
    while que:
        v = que.popleft() # 큐에서 정점하나 꺼내기 
        if not visited[v]: # 아직 방문하지 않은 정점인경우 
            visited[v] = True # 정점 방문처리 
            result.append(v)  # 방문한 정점 기록
            for u in G[v]:  # 현재 정점 v에 연결된 모든 정점 u에대해 
                if not visited[u]:  # 아직 방문하지 않은 정점만 추가
                    que.append(u) # 큐에 정점 u추가
    
    return result

# DFS 함수 정의
def dfs(v, visited, result):
    visited[v] = True  # 현재 정점 방문 처리
    result.append(v)   # 방문한 정점 기록
    for u in G[v]:     # 현재 정점에 연결된 모든 정점 u에 대해
        if not visited[u]:  # 아직 방문하지 않은 정점
            dfs(u, visited, result)  # 재귀적으로 DFS 수행


# BFS 실행
result = bfs(s)
visited = [False] * (n + 1)  # 방문 여부를 저장하는 리스트
res = []
dfs(s, visited, res)  # s에서 DFS 시작

# 결과 출력
print(" ".join(map(str, res)))
# 결과 출력
print(" ".join(map(str, result)))