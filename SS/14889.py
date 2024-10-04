import sys
sys.stdin = open("input.txt", 'r')

def dfs(L, idx):
    # 1. 종료조건: N//2
    global ans
    if L == N//2:
        # 계산: visited True, False 나눠서 차이값 ans = min(ans, 새로 구한 값)
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += P[i][j]
                elif not visited[i] and not visited[j]:
                    B += P[i][j]
        ans = min(ans,abs(A-B))
        return

    # 2. 하부 호출: 현재 인덱스 부터 하부 호출
    for i in range(idx, N): # A잡고 AB, AC, AD 구하면 한 바퀴, 다음은 B
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1) #i는 이미 방문했으니 +1 해서 중복 없는 조합으로
            visited[i] = False # 백트래킹

if __name__ == "__main__":
    # 입력 받기
    N = int(input())
    P = [0]*N

    for i in range(N):
        P[i] = [*map(int, input().split())]

    visited = [False] * N
    ans = 99999 #INF

    dfs(0, 0)

    # 출력
    print(ans)