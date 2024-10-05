import sys
sys.stdin = open("input.txt", "r")

N = int(input())
A = [*map(int, input().split())]
C = [*map(int, input().split())]

# 초기값
op = -1
cnt = 0
temp = A[0]
maxans = -10**9
minans = 10**9

def dfs(op, cnt, temp):
    global maxans, minans
    # 계산
    if op == 0: # 덧셈
        temp = temp+A[cnt]
    if op == 1: # 뺄셈
        temp = temp-A[cnt]
    if op == 2: #곱셈
        temp = temp*A[cnt]
    if op == 3: #나눗셈
        if temp < 0:
            temp = -(abs(temp)//A[cnt])
        else: 
            temp = temp // A[cnt]

    # 종료
    if cnt == N-1:
        maxans = max(maxans, temp)
        minans = min(minans, temp)
        return

    # 호출 조건: 사용 가능한 연산자가 있을 때
    for i in range(4):
        if C[i] > 0:
            C[i] -= 1
            dfs(i, cnt+1, temp)
            C[i] += 1

dfs(op, cnt, temp)

print(maxans)
print(minans)