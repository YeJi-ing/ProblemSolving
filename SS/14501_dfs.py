# 이진트리 문제면 대략 50까지는 시간 초과 없이 가능: 2의 50승
# 이진트리의 마지노선이 2의 50승

import sys
sys.stdin = open("input.txt", "r")

# global은 수정할 때 사용. N,P,T는 읽기만 하고 있어서 global 키워드 사용하지 않았다.
# return을 마주하면 종료되고, 호출된 지점으로 돌아간다. == 그러니 가장 깊은 곳 부터 return 되는 깊이 우선 탐색(DFS)
def dfs(n, sm):
    global ans
    # 1. 종료조건: 가능한 n을 종료에 관련된 것으로 정의!
    if n>=N:
        ans = max(ans, sm)
        return
    
    # 2. 하부호출: 화살표 개수만큼 호출
    if n+T[n] <= N: # 상담하는 경우 (퇴사일 전 완료 가능할 때만 상담)
        dfs(n+T[n], sm+P[n])

    # 상담 하지 않는 경우 (항상 가능)
    dfs(n+1, sm)


N = int(input())
T = [0]*N #리스트
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0,0)
print(ans)