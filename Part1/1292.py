import sys
sys.stdin = open("input.txt", 'r')

A, B = map(int, input().split())

step = 0
cnt  = 0
ans = 0
while True:
    for i in range(cnt):
        #print(cnt)
        step += 1
        if step >= A and step <= B:
            ans += cnt
    cnt += 1

    if step > B:    break

print(ans)