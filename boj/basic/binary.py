from sys import stdin

T = int(stdin.readline())
N = []
for t in range(T):
    N.append(int(stdin.readline()))

for n in N:
    binary = []
    indexes = []

    while(n >= 1):
        remain = n % 2
        if remain == 1:
            indexes.append(str(len(binary)))
        binary.insert(0, remain)
        n = n // 2

    print(" ".join(indexes))