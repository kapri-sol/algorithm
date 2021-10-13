H, W = map(int, input().split())
blocks = list(map(int, input().split()))

left = 0
right = W - 1

maxLeft = 0
maxRight = 0

result = 0

while left < right:
    maxLeft = max(maxLeft, blocks[left])
    maxRight = max(maxRight, blocks[right])

    if maxRight >= maxLeft:
        result += maxLeft - blocks[left]
        left += 1
    else :
        result += maxRight - blocks[right]
        right -= 1

print(result)