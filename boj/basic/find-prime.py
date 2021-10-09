from sys import stdin

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

def checkIsPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(sum(map(checkIsPrime, nums)))

