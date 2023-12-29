import sys
input = sys.stdin.readline

def round_new(n):
  return int(n) + (1 if n - int(n) >= 0.5 else 0)

n = int(input())
b = round_new(n * 0.15) # 사사오입

if n == 0:
  print(0)
else:
  score = []
  for _ in range(n):
    score.append(int(input()))
  score.sort() # 크기순 나열

  sum = 0
  for i in range(b, n - b):
    sum += score[i]
  avg = sum / (n - 2*b)
  print(round_new(avg))
