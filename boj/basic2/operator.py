N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

minNum = 1000000000
maxNum = -1000000000

def calculate(opIdx, left, rigth):
    if opIdx == 0:
        return left + rigth
    elif opIdx == 1:
        return left - rigth
    elif opIdx == 2:
        return left * rigth
    elif opIdx == 3:
        return int(left / rigth)

def dfs(idx, acc):
    if idx == len(nums) - 1:
        global minNum
        global maxNum

        minNum = min(minNum, acc)
        maxNum = max(maxNum, acc)
        return

    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            dfs(idx + 1, calculate(i, acc, nums[idx + 1]))
            ops[i] += 1

dfs(0, nums[0])

print(maxNum)
print(minNum)