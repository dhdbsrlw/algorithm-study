import sys
input = sys.stdin.readline

n = int(input())
string = input()
string = list(string)

answer = 0

for i in range(n):
    answer += (ord(string[i]) - 96) * (31 ** i) # 'a'에 해당하는 격이 96
    
print(answer % 1234567891)