from sys import stdin

talls = []

for t in range(9):
    talls.append(int(stdin.readline()))

talls.sort()

for firstTall in  talls:
    for secondTall in talls:
        if firstTall == secondTall:
            continue
        if (sum(talls) - (firstTall + secondTall)) == 100:
            talls.remove(firstTall)
            talls.remove(secondTall)
            break

for tall in talls:
    print(tall)