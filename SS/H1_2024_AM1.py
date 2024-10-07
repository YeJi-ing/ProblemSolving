import sys
from traceback import print_exc

sys.stdin = open("input.txt", 'r')

# 반복 횟수 K와 벽면에 적힌 유물 조각의 개수 M
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
mnum = [*map(int, input().split())]

ans = [] # 출력

def rotation(arr, si, sj):
    narr = [x[:] for x in arr]
    # si, sj를 기준으로 3x3 배열 90도 회전
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+3-j-1][sj+i]
    return narr

def bfs(narr, v, si, sj, mod):
    # i j 에서 가지는 가치값 return
    q = []
    sset = set() # 0으로 만들 좌표들 저장
    cnt = 0

    q.append((si,sj))
    v[si][sj] = 1
    sset.add((si, sj))
    cnt += 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
            ni = ci + di
            nj = cj + dj
            # 조건: 범위내, 방문 안 함, 나랑 숫자 같음
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and narr[ci][cj]==narr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
                sset.add((ni, nj))
    if cnt < 3:
        return 0
    else:
        if mod == 1:
            for i, j in sset:
                arr[i][j] = 0
        return cnt

def value_count(narr, mod):
    # narr의 모든 i, j를 호출시켜서 return 값 더하는 함수
    v = [[0]*5 for _ in range(5)] # 방문한 곳들 1표시, 같은 수들은 이미 방문하게 되니까
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                t = bfs(narr, v, i, j, mod)
                cnt += t
    return cnt

for _ in range(K):
    max_cnt = 0
    marr  = None
    # 우선 순위: 회전한 각도(작은 순) -> 열 작은 순 -> 행 작은 순
    for rot in range(1, 4): # rot가 1번 돌면 90도 회전, 2번 180도, 3번 270도
        for j in range(3):
            for i in range(3):
                narr = [x[:] for x in arr]
                # 실제 회전
                for _ in range(rot):
                    narr = rotation(narr, i , j)

                # 그 arr의 최대 가치값
                #print(narr)
                t = value_count(narr,0) # 실제 v를 바꾸지 마
                if t > max_cnt:
                    max_cnt = t
                    marr = narr

    if max_cnt == 0:
        break

    arr = marr
    cnt = 0

 # 그 회전 맵에서 가치 값 찾고 인덱스 삭제 후 보충.. 가치가 0이 될 때 까지
    while True:
        # 가치 값 찾고, 실제 0으로 매핑
        t = value_count(arr,1) # 실제 v를 바꿔
        if t == 0:
            break # 다음 턴으로
        else:
            cnt += t

            # 열 번호가 작은 순 -> 행 번호가 큰 순
            for j in range(5):
                for i in range(4, -1, -1): # 4 3 2 1 0
                    if arr[i][j] == 0:
                        arr[i][j] = mnum.pop(0)
    ans.append(cnt)
print(*ans)
