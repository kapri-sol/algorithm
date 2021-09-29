from sys import stdin

N = stdin.readline()
nums = list(map(int, stdin.readline().split()))

min = 1000001
max = -1000001

for n in nums:
    if n < min:
        min = n
    if n > max:
        max = n

print(min, max)