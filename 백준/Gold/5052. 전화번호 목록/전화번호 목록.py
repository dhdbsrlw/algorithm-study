import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())

  phone = []
  for _ in range(n):
    phone.append(input().rstrip())

  phone.sort() # 접두사가 같은 것들은 인근에 위치
  
  ans = True
  for i in range(len(phone) - 1):
    if phone[i] == phone[i+1][:len(phone[i])]:
      ans = False
      break
      
  print('YES') if ans else print('NO')