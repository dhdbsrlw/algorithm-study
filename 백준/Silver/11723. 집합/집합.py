import sys
input = sys.stdin.readline

m = int(input())
s = set() # 리스트 대신 셋 사용

for _ in range(m):
  fullcmd = (input().rstrip()).split()

  # 인자가 없는 명령어 고려 필요
  if len(fullcmd) == 1:
    if fullcmd[0] == 'all':
      s = set([i for i in range(1, 21)])
    else: # = empty
      s = set()
  
  else:
    cmd, num = fullcmd[0], int(fullcmd[1])
    
    if cmd == 'add':
      s.add(num)
    elif cmd == 'remove' and num in s:
      s.discard(num) # valueError 방지 위해 remove 를 discard 로 대체
    elif cmd == 'check':
      print(1) if num in s else print(0)
    elif cmd == 'toggle':
      s.discard(num) if num in s else s.add(num)