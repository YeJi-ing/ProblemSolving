import sys

sys.stdin = open("input.txt", 'r')

# input ---------------------------
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [[1]*(M+2)] + [ [1]+list(map(int, input().split()))+[1] for _ in range(N) ] + [[1]*(M+2)] # 0:청소X, 1:벽, 2:청소O
r, c = r+1, c+1

# prepare -------------------------
# 북 동 남 서
di = [-1, 0, 1,  0]
dj = [ 0, 1, 0, -1]
ans = 0

# main ---------------------------
while True:
    if arr[r][c] == 0: # 현재 칸이 청소 되지 않은 경우 현재 칸 청소
        arr[r][c] = 2
        ans += 1
    elif arr[r+di[0]][c+dj[0]] == 0 or arr[r+di[1]][c+dj[1]] == 0 or arr[r+di[2]][c+dj[2]] == 0 or  arr[r+di[3]][c+dj[3]] == 0:
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸 있음
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전
        ni, nj = r+di[d], c+dj[d]
        if arr[ni][nj] == 0: # 청소X 이면 전진
            r, c = ni, nj
    else:
        ni, nj = r - di[d], c - dj[d]
        if arr[ni][nj] != 1: # 벽이 아니면 후진
            r, c = ni, nj
        else: # 벽이면 중지
            break

# output -------------------------
print(ans)
