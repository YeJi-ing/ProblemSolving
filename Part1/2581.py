import sys
sys.stdin = open("input.txt", 'r')

M = int(input())
N = int(input())
ans_sum = 0
ans_min = 10000

for i in range(M, N+1): # M 이상 N 이하
    non = 0
    for j in range(2, i):
        if i % j == 0:
            non = 1
            break
    if non == 0: # 소수
        ans_sum += i
        if ans_min > i:
            ans_min = i

if ans_sum == 0:
    print(-1)
else:
    print(ans_sum)
    print(ans_min)
