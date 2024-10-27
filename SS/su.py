import sys

sys.stdin = open("input.txt", 'r')

# input ---------
def coverlist(x):
    x = int(x)
    if x!= 0:
        return [x]
    else:
        return []

n, m, k = map(int, input().split())
arr = [list(map(coverlist, input().split())) for _ in range(n)] # 3차원 배열 append, remove
unitsarr = [[[] for _ in range(n)] for _ in range(n)] # 3차원 배열

units = {} # 1 ~ m+1
for i in range(1, m+1):
    x, y, d, s = map(int, input().split())
    x, y = x-1, y-1
    unitsarr[x][y] = i
    units[i] = x, y, d, s, 0 # 초기에 가지고 있는 총 능력치 0
score = [0]*(m+1)

# prepare ---------------------
di = [-1, 0, 1,  0] # 상 우 하 좌
dj = [ 0, 1, 0, -1]

# def ------
def win(a):
    """

    :param a:
    :return:
    """
def

def fight(i, j):
    """
    원래 있던 것과 새로온 것 싸움
    i, j: 현재 위치
    """
    one, two = unitsarr[i][j]
    oi, oj, od, os, og = units[one]
    ti, tj, td, ts, tg = units[two]




def gunchose(idx):
    global arr, units
    xi, xj, xd, xs, xg = units[idx]
    value = arr[xi][xj]

    if not value: return # 총 없음
    maxgun = max(value)
    if xg >= maxgun: return # 총 있는데 보유한 총 보다 능력치 작음
    arr[xi][xj].append(xg) # 가지고 있던 총 두고
    arr[xi][xj].remove(maxgun) # 공격력이 더 쎈 총을 획득
    units[idx] = xi, xj, xd, xs, maxgun # units에 총 업데이트
    return

# main ----------
for _ in range(k):
    for man in range(1, m+1): # 첫 번째 ~ 마지막 사람 순
        # [1] 이동
        print(unitsarr)
        ui, uj, ud, us, ug = units[man]
        ni, nj = ui + di[ud], uj + dj[ud]
        if 0>ni or ni>=n or 0>nj or nj>=n: # 격자 벗어나는 경우
            ni, nj = ui + di[(ud+2)%4], uj + dj[(ud+2)%4]
        # 위치 업데이트 - unitarr
        units[man] = ni, nj, ud, us, ug
        unitsarr[ui][uj] = 0  # 원래 위치 0
        unitsarr[ni][nj] = man
        # 사람 없음
        if unitsarr[ni][nj] == 0:
            unitsarr[ni][nj] = man # unitarr에 이동 업데이트
            gunchose(man) # 총 처리
            print(unitsarr)
        else: # 사람 있음
            fight()
            # [2] 승패 가르기
            someone = unitsarr[ni][nj]
            si, sj, sd, ss, sg = units[someone]
            fight = (us+ug) - (ss+sg)
            if fight == 0: # win 업데이트
                if us > ss:
                    win, lose = man, someone
                    unitsarr[ni][nj] = man
                    units[man] = ni, nj, ud, us, ug
                    unitsarr[si][sd] = 0  # 원래 위치 0
                    fi, fj, fd, fs, fg = si, sj, sd, ss, sg
                else:
                    win, lose = someone, man
                    #unitsarr[ni][nj] = someone
                    #units[someone] = si, sj, sd, ss, sg
                    fi, fj, fd, fs, fg = ni, nj, ud, us, ug
            elif fight > 0: # 온 애가 더 세다
                win, lose = man, someone
                unitsarr[ni][nj] = man
                units[man] = ni, nj, ud, us, ug
                unitsarr[si][sd] = 0  # 원래 위치 0
                fi, fj, fd, fs, fg = si, sj, sd, ss, sg
            elif fight < 0:
                win, lose = someone, man
                #unitsarr[ni][nj] = someone
                #units[someone] = si, sj, sd, ss, sg
                fi, fj, fd, fs, fg = ni, nj, ud, us, ug
            score[win] += abs(fight) # 스코어
            print(unitsarr)

            arr[fi][fj].append(fg) # 총 내려놓고
            for i in range(4): # lose 이동 업데이트
                fni, fnj = fi + di[(fd+i)%4], fj + dj[(fd+i)%4]
                if 0<=fni<n and 0<=fnj<n and unitsarr[fni][fnj] == 0: # 사람 없고, 격자 안
                    unitsarr[fni][fni] = lose
                    units[lose] = fni, fnj, fd, fs, fg
                    print(unitsarr)
                    gunchose(lose) # lose 총 처리
                    break
            gunchose(win) # win 총 처리

# output --------
print(*score[1:])