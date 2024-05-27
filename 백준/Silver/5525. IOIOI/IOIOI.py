import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
s = input().strip()

idx, cnt, result = 0, 0, 0

while idx < (m - 1):
    if s[idx:idx + 3] == 'IOI': # 3칸
        cnt += 1
        idx += 2
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(result)