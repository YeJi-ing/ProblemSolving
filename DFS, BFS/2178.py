import sys
sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
# 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸
arr = [[0]*(M+2)] + [[0] + list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]

#    북  서   남   동
di = [-1,  0,  1,  0]
dj = [ 0, -1,  0,  1]

visited = [[0]*(M+2) for _ in range(N+2)]

visited[1][1] = 1
minans = 100**2

def dfs(si, sj, temp):
    global minans
    if (si, sj) == (N,M):
        minans = min(minans, temp)
        return

    for i in range(4): # 북 서 남 동
        ni, nj = si + di[i], sj + dj[i]
        if visited[ni][nj] == 0 and arr[ni][nj] == 1: # 이동할 수 있는 칸
            visited[ni][nj] = 1
            dfs(ni, nj, temp+1) # 내 temp는 그대로이고 재귀의 temp에 +1
            visited[ni][nj] = 0

dfs(1, 1, 1) # 1, 1에서 시작, 시작위치 포함
print(minans)

#print(arr[N][M])
