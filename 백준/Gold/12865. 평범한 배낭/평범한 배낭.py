import sys
input = sys.stdin.readline

n, k = map(int, input().split())
obj = [[0,0]]
table = [[0 for _ in range(k+1)] for _ in range(n+1)] # 2차원 배열, k+1 행, n+1 열

# 물건 리스트
for _ in range(n):
  obj.append(list(map(int, input().split())))

for i in range(1, n+1):
  w = obj[i][0]
  v = obj[i][1]
  for j in range(1, k+1):
    if j < w:
      table[i][j] = table[i-1][j]
    else:
      table[i][j] = max(v + table[i-1][j-w], table[i-1][j])

print(table[n][k])