import sys

sys.stdin = open("input.txt", 'r')

# (0,1,2,3: 북, 동, 남, 서)
di = [-1, 0, 1,  0]
dj = [ 0, 1, 0, -1]

# 숲의 크기 R, C, 정령의 수 K
R, C, K = map(int, input().split())

unit = [list(map(int, input().split())) for _ in range(K)] # 2차원 배열
arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
exit_set = set() # 출구 좌표

def bfs(si, sj):
    q = []
    v = [[0]*(C+2) for _ in range(R+4)] # visited
    mx_i = 0 # -2해서 리턴!

    q.append((si, sj))
    v[si][sj]=1 # 표시

    while q:
        ci, cj = q.pop()
        mx_i = max(mx_i, ci)

        # 가는 경우: 네방향, 미방분, 조건: 같은 값 또는 내가 출구 - 상대방이 골렘
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj+dj # 갈 좌표 (일단 방문 안함) and ((내 골룸 안) or (내 출구 좌표, 상대방 좌표))
            if v[ni][nj]==0 and (arr[ci][cj]==arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj]>1)):
                q.append((ni, nj))
                v[ni][nj]=1

    return mx_i-2

ans = 0 # 결과s
num = 2 # 골렘 번호
# 골렘 입력 좌표/방향에 따라서 남쪽이동 및 정령 최대좌표 계산
for cj, dr in unit:
    ci = 1 # 초기값
    while True:
        # 1. 남쪽으로 최대한 이동 (남쪽 -> 서쪽 -> 동쪽)
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
            ci += 1 # 남쪽
        elif arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1] + arr[ci+1][cj-2]+arr[ci+2][cj-1] == 0:
            ci+=1 # 남쪽
            cj-=1 # 서쪽
            dr = (dr-1)%4 # 왼쪽으로 회전
        elif arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+1][cj+2]+arr[ci+2][cj+1] == 0:
            ci+=1 # 남쪽
            cj+=1 # 동쪽
            dr = (dr+1)%4 # 오른쪽으로 회전
        else:
            break

    # [2] 골렘을 표시 + 비상구 위치 추가
    if ci<4: # 몸이 범위 밖 (새롭게 탐색 시작.. arr 등 모두 초기화)
        arr = [[1]+ [0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)] # 초기화
        num = 2 # 초기화
        exit_set = set() # 초기화
    else:
        # 나를 표시
        arr[ci+1][cj]=arr[ci-1][cj]=num
        arr[ci][cj-1:cj+2]=[num]*3
        num += 1

        exit_set.add((ci+di[dr], cj+dj[dr])) # 출구는 골렘 위치에서 dr만큼 간 위치
        ans += bfs(ci, cj)

print(ans)