from sys import stdin

num1, num2 = map(int, stdin.readline().split())

def gcd(num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)
    mod = big % small

    if mod == 0:
        return small
    else:
        return gcd(small, mod)

gcf = gcd(num1, num2)
lcm = num1 * num2 // gcf

print(gcf)
print(lcm)