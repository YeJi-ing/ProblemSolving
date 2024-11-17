import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
dp = [[0] * 2 for _ in range(n + 1)]

# 초기값 설정
dp[1][0] = 0
dp[1][1] = 1

# 점화식을 기반으로 DP 테이블 채우기
for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

# 결과 출력
print(dp[n][0] + dp[n][1])