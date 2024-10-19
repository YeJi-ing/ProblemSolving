import sys
sys.stdin = open("input.txt", 'r')

#     북  동 남  서
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

# input ----------------------------
R, C, K = map(int, input().split())
units = {} # 최종 위치와 출구 저장: i, j

# prepare --------------------
# 0: 빈공간, 1: 벽, 1~k+1: 골렘
arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
num = 2 # 골렘 시작 번호
exit_set = set() # 출구 위치
ans = 0

# def --------------------
def bfs(idx):
    """
    idx: arr[ui][uj]의 값
    ui, uj에서 가장 큰 행으로 이동
    return max_i-2
    """
    ui, uj = units[idx]
    q = []
    v = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
    max_i = 0 # 가장 큰 행
    q.append((ui, uj))

    while q:
        pi, pj = q.pop()
        max_i = max(max_i, pi)

        # 방문 안함, (범위 내 - 지금은 1로 감쌌다) and
        # 자신의 골렘 안에서 가장 행 큰 곳으로 or
        # 현재 위치가 출구, 다음 위치가 다른 골렘 안
        for i in range(4):
            ni, nj = pi+di[i], pj+dj[i]
            if v[ni][nj]==0 and (arr[pi][pj]==arr[ni][nj] or ((pi, pj) in exit_set and arr[ni][nj]>=2)):
                v[ni][nj] = 1
                q.append((ni, nj))

    return max_i-2

# main --------------------
for idx in range(K): # 0~k-1
    sj, d = map(int, input().split())
    sj -= 1
    si = 1
    ci, cj = 0, 0
    while True:
        if arr[si+1][sj-1]==0 and arr[si+2][sj]==0 and arr[si+1][sj+1]==0: # 남쪽 3칸
            si += 1
        elif arr[si-1][sj-1]==0 and arr[si][sj-2]==0 and arr[si+1][sj-1]==0 and arr[si+1][sj-2]==0 and arr[si+2][sj-1]==0:
            si += 1
            sj -= 1
            d = (d-1)%4
        elif arr[si-1][sj+1]==0 and arr[si][sj+2]==0 and arr[si+1][sj+1]==0 and arr[si+1][sj+2]==0 and arr[si+2][sj+1]==0:
            si += 1
            sj += 1
            d = (d+1)%4
        else: # 더이상 이동 불가
            break
    # 위치 확정
    if si < 4: # 꽉참
        # 초기화
        arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
        num = 2 # 골렘 시작 번호
        exit_set = set() # arr 안 있는 출구 초기화
        units = {} # arr 안 골렘 초기화
    else:
        # units, exits_set 추가
        units[num] = [si, sj]
        exit_set.add((si+di[d], sj+dj[d]))
        # arr에 골렘 위치 표시
        arr[si][sj] = num
        for i in range(4): # 양 방향
            arr[si+di[i]][sj+dj[i]] = num
        # 갈 수 있는 가장 남쪽으로 이동
        mx_i = bfs(num)
        # 최종적으로 위치한 행의 총합
        ans += mx_i
        # 다음 골렘 num
        num += 1

# output ----------------------------
print(f'#테스트케이스번호 {ans}')