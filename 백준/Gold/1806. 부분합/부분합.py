import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터의 2가지 유형 중 특정 값을 넘는 배열에 대해서 구하면 된다.
# 누적 값이 S보다 크다면 개수를 따져주고 왼쪽 포인터를 1 늘린다.
# S보다 작다면 오른쪽 포인터를 1 늘린다.

# 이른 종료
if s == 1:
  print(1) # 시간초과시 삭제예정

else: 
  # 이른 종료
  if sum(arr) < s:
    print(0) # 시간초과시 삭제예정

  elif max(arr) >= s:
    print(1) # 시간초과시 삭제예정
    
  # 일반 케이스
  else:
    # 초기 세팅
    lidx = 0
    ridx = 1
    sum = arr[lidx] + arr[ridx]
    ans = 100000
    
    while (True):
      if sum < s:
        ridx += 1
        if ridx == n: # 배열의 끝 도달
          break
        sum += arr[ridx]
        if sum >= s and (ridx - lidx + 1) < ans:
          ans = ridx - lidx + 1 # 중간 기록
          if ans == 2:
            break

      else:
        sum -= arr[lidx]
        lidx += 1
        if sum >= s and (ridx - lidx + 1) < ans:
          ans = ridx - lidx + 1 # 중간 기록
          if ans == 2:
            break
        if lidx == n or lidx > ridx:
          break
          
    print(ans)