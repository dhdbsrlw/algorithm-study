import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  s = list(input().rstrip())
  
  start = 0
  end = len(s) - 1
  flag = 0

  while(start < end):
    
    if s[start] == s[end]:
      start += 1
      end -= 1
      
    else:        
      # 유사회문 여부 확인 - 한쪽 문자 제거 후 회문인지 확인
      # 오른쪽 문자 제거
      if start <= end - 1:
        tmp = s[:end] + s[end + 1:]
        if tmp[:] == tmp[::-1]: # 리버스와 일치 (=회문)
          flag = 1
          break

      # 왼쪽 문자 제거
      if start + 1 <= end:
        tmp = s[:start] + s[start + 1:]
        if tmp[:] == tmp[::-1]:
          flag = 1
          break

      flag = 2
      break
      
  print(flag)