import sys
sys.stdin = open("input.txt", 'r')

N = int(input())
arr = [*map(int, input().split())]
ans = 0

for i in range(N):
    non = 0
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            non += 1
            break
    if arr[i]>1 and non == 0: # 소수
        ans += 1

print(ans)