import sys
input = sys.stdin.readline

num = list(input().rstrip())
num.sort(reverse=True)
num = "".join(num)
print(num)
