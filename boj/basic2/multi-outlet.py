N, K = map(int, input().split())
products = list(map(int, input().split()))

outlet = []
cnt = 0

for k in range(K):
    if products[k] in outlet:
        continue

    if len(outlet) < N:
        outlet.append(products[k])
        continue

    lru = []

    for n in range(N):
        if outlet[n] in products[k:]:
            lru.append(products[k:].index(outlet[n]))
        else:
            lru.append(K - k)

    cnt += 1
    outlet[lru.index(max(lru))] = products[k]

print(cnt)