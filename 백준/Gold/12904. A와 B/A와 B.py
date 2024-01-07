import sys
from collections import deque
input = sys.stdin.readline

s = deque(input().strip())
t = deque(input().strip())
len_s = len(s)
len_t = len(t)

while(len_s < len_t):
  if t[-1] == 'A':
    t.pop()
    len_t -= 1
  else: # = 'B'
    t.pop()
    len_t -= 1
    t.reverse()

print(1) if s == t else print(0)