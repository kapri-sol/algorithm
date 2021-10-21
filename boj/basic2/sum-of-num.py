N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
sumOfNums = 0

while end <= N:
    if sumOfNums == M:
        cnt += 1

    if sumOfNums < M:
        if end == N:
            break
        sumOfNums += nums[end]
        end += 1
    elif sumOfNums >= M:
        sumOfNums -= nums[start]
        start += 1

print(cnt)