import sys
from collections import deque
input = sys. stdin.readline

n = int(input())
q = deque([])
ans = 0

# 입구
for _ in range(n):
  car_in = input().rstrip()
  q.append(car_in)

# 출구
cur = q.popleft()
for _ in range(n):
  car_out = input().rstrip()
  if car_out == cur:
    if q:
      cur = q.popleft()
    else:
      break # 마지막
  else:
    ans += 1
    q.remove(car_out) # 처리 필요

print(ans)