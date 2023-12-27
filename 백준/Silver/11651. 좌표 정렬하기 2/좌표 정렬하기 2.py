import sys
# import heapq

input = sys.stdin.readline
arr = []

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  arr.append([y, x]) # y 기준 정렬

arr = sorted(arr)
for pair in arr:
  print(pair[1], pair[0])