import sys
# input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
  
  word = input()
  table = [0] * 26 # 단어마다 초기화 필요
  flag = True # 단어마다 초기화 필요
  
  if len(set(word)) == len(word):
    cnt += 1
    continue

  else:
    latest = ''
    
    for w in word:
      idx = ord(w) - 97
      table[idx] += 1
      
      if table[idx] > 1:
        if latest != w:
          flag = False
          break
      else:
        latest = w

    if flag is True:
      cnt += 1

print(cnt)
