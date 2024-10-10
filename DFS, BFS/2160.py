import sys
sys.stdin = open("input.txt", 'r')

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 1번 정점부터 N번 정점까지 사용하기 위해 N+1 크기

# M개의 간선 정보 입력
# [[], 1 -> [2, 3, 4], 2 -> [1, 4], 3 ->[1, 4], 4 -> [1, 2, 3]]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 간선이므로 양쪽에 추가
    graph[a].sort() # 작은 것 부터
    graph[b].sort() # 작은 것 부터

visited = [False]*(N+1)
dfslst = []
def dfs(graph, v, visited):
    visited[v] = True
    dfslst.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited)
print(*dfslst)

visited = [False]*(N+1)
bfslst = []
def bfs(graph, v, visited):
    q = []
    
    q.append(v)
    visited[v] = True
    bfslst.append(v)

    while q:
        cur = q.pop(0)

        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                bfslst.append(i)

bfs(graph, V, visited)
print(*bfslst)

