from sys import stdin

maxCnt = -1
current = 0

for i in range(10):
    left, ride = map(int, stdin.readline().split())
    current = current - left + ride
    maxCnt = max(maxCnt, current)

print(maxCnt)