import sys

# lcs 알고리즘 활용

str1 = input()
str2 = input()
dp = [[0] * 4001 for _ in range(4001)]
answer = 0

for i in range(1, len(str1) + 1):
  for j in range(1, len(str2) + 1):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1 # dp 테이블 업데이트
      if dp[i][j] > answer:
        answer = dp[i][j]
      
print(answer)