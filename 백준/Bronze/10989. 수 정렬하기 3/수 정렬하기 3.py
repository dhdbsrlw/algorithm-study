import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * (10000 + 1) # 최대값 10000

for _ in range(n):
  a = int(input())
  cnt[a] += 1

for idx, i in enumerate(cnt):
  if i != 0 :
    for _ in range(i):
      print(idx)
  
# 메모리에 제약이 있는 경우, 계수 정렬 활용