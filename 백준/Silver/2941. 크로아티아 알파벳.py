import sys
#input = sys.stdin.readline
# 문자열 문제에서는 위 readline 을 사용하지 않는 것이 좋다. input 받을 때 자동으로 마지막에 개행문자를 추가시킨다. 

table = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'dz=', 'z='] # 총 8개
text = input()
answer = len(text) # 초기화

for word in table:
  cnt = text.count(word)
  if word == 'z=': # 예외처리
    tmp = text.count('dz=')
    cnt -= tmp
    
  #print(cnt)
  if cnt == 0:
    pass
  else:
    answer -= cnt if word != 'dz=' else (2 * cnt)

print(answer)
