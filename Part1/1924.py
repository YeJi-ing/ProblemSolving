import sys
sys.stdin = open("input.txt", 'r')

x, y = map(int, input().split())

arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

days_elapsed = sum(arr[:x-1]) + (y - 1)
ans = days[days_elapsed % 7]

print(ans)
