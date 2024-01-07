import sys
input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))


arrA.sort() 
arrB.sort(reverse=True) # 큰 수부터 정렬
S = 0

# S 의 최솟값
for i in range(n):
  S += (arrA[i] * arrB[i])

print(S)