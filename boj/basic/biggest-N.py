from sys import stdin

T = int(stdin.readline())
N = 3
for t in range(T):
    nums = list(map(int, stdin.readline().split()))
    nums.sort(reverse=True)
    print(nums[N-1])