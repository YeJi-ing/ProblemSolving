import sys
sys.stdin = open("input.txt", 'r')

# 입력 받기
N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1) #초기값
for n in range(N-1, -1, -1): # 뒤부터
    # 퇴사 전 상담완료 가능
    if n+T[n] <= N: 
        dp[n] = max((dp[n+T[n]]+P[n]), dp[n+1])
    else: # 퇴사 전 상담완료 불가능
        dp[n] = dp[n+1]

print(dp[0])
