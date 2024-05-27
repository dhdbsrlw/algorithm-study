import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
s = input().strip()

txt = "I" + ("OI" * n)
cnt = 0
idx = 0

while(1):
  idx = s.find(txt)
  if idx != -1:
    cnt += 1
    s = s[idx+2:]
  else:
    break
    
print(cnt)