from sys import stdin

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonachi(n - 1) +fibonachi(n - 2)

print(fibonachi(int(stdin.readline())))