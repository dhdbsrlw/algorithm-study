import sys 
import heapq 
input = sys.stdin.readline

n = int(input())
smaller = []
bigger = []
ans = []

for i in range(n):
  
  num = int(input())

  if len(smaller) == len(bigger):
    heapq.heappush(smaller, (-num, num)) # (우선순위, 값)
  else:
    heapq.heappush(bigger, (num, num))


  if bigger and smaller[0][1] > bigger[0][1]: # 2 개를 스위치
    min = heapq.heappop(bigger)[1]
    max = heapq.heappop(smaller)[1]
    heapq.heappush(smaller, (-min, min))
    heapq.heappush(bigger, (max, max))

  ans.append(smaller[0][1])

for _ in ans:
  print(_)