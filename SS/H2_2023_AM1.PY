import sys
sys.stdin = open("input.txt", "r")

# 2차원 배열에서 네 가지 방향으로 이동 위해
# 방향: 상 우 하 좌
di = [-1, 0, 1,  0] # 행 변화 (x), -1이면 위로, 1이면 밑으로
dj = [ 0, 1, 0, -1] # 열 변화 (y), -1이면 왼쪽, 1이면 오른쪽

# 체스판 크기, 기사 수, 명령 수
N, M, Q = map(int, input().split())

# 벽으로 둘러싸서, 범위 체크 안하고, 범위 밖으로 밀리지 않게 처리
arr = [[2]*(N+2)] + [[2]+ list(map(int, input().split())) +[2] for _ in range(N)] + [[2]*(N+2)]

# 살아있는 병사들의 스펙
units = {}
init_k = [0]*(M+1) # 초기 체력값 
for m in range(1, M+1):
    si,sj,h,w,k=map(int, input().split())
    units[m]=[si, sj, h, w, k]
    init_k[m]=k

def push_units(start, dr):
    # 미는 기능을 수행. 이때 연쇄처리가 된다.
    # 1. 민다고 하면 밀어지는 지 (안되는 경우: 벽인 경우), 유닛 별 데미지 값 누적
    # 2. 밀어지는 경우에 한해서, 겹치는 다른 유닛이 있는 경우 큐에 추가
    # 3. 이동, 데미지 처리(데미지가 체력 이상이면 삭제 처리)

    # 데미지 값 누적하는 변수, 이 데미지는 받을 수도 있고 안 받을 수도 있으니까 유닛별 저장
    # 겹치는 유닛 큐에 저장

    q = []           # push 후보를 저장 
    pset = set()     # 이동 기사번호 저장
    damage = [0]*(M+1) # 각 유닛별 데미지 누적

    q.append(start) # 초기 데이터 append
    pset.add(start)

    while q: # pset을 구하자
        cur = q.pop(0)   # q에서 데이터 한 개 꺼냄
        #print(units[cur])
        ci,cj,h,w,k = units[cur]

        # 명령받은 방향으로 진행, 벽이 아니면, 겹치는 다른 조각이면 => 큐에 삽입
        ni = ci+di[dr]
        nj = cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j]==2: # 벽!
                    return 
                if arr[i][j]==1: # 함정인 경우
                    damage[cur]+=1
        
        # 연쇄적인 밀림, 겹치는 다른 유닛이 있는 경우 큐에 추가 (모든 유닛 체크)
        for idx in units:
            if idx in pset: continue   # 이미 움직일 대상이면 체크할 필요없음

            ti,tj,th,tw,tk=units[idx]

            # 겹치는 경우! 한 칸이라도 겹치면 밑의 조건문 다 충족함
            if ni<=ti+th-1 and ni+h-1>=ti and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(idx)
                pset.add(idx)
                
    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0

    # 이동, 데미지가 체력 이상이면 삭제 처리
    for idx in pset:
        si,sj,h,w,k = units[idx]

        if k<=damage[idx]: # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni = si + di[dr]
            nj = sj + dj[dr]
            # i, j, 데미지 업데이트
            units[idx] = [ni, nj, h, w, k-damage[idx]]


# 명령 입력 받고 처리 (있는 유닛만 처리)
for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_units(idx, dr)  # 명령받은 기사(연쇄적으로 밀기: 벽이 없는 경우)


ans = 0 # 생존한 기사들이 총 받은 대미지의 합을 출력
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)