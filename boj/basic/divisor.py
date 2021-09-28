from sys import stdin

N, K = map(int, stdin.readline().split())

k = 0

for i in range(N):
    if N % (i + 1) == 0:
        k = k + 1
    if k == K:
        print(i + 1)
        break;

if k < K:
    print(0)