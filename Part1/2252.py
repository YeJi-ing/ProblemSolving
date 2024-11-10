import sys
import heapq
input = sys.stdin.read

def topological_sort(n, edges):
    # 진입 차수 및 그래프 초기화
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    # 그래프 구축 및 진입 차수 계산
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1

    # 위상 정렬을 위한 우선순위 큐 (작은 숫자 우선)
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    result = []
    while heap:
        current = heapq.heappop(heap)
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    return result

# 입력
data = input().strip().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:]]

# 위상 정렬 수행
result = topological_sort(n, edges)

# 결과 출력
print(" ".join(map(str, result)))