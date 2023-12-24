import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수 (정점)
m = int(input()) # 노선의 개수 (간선) 
INF = sys.maxsize
graph = [[INF] * (n+1) for _ in range(n+1)] 

# 인접행렬 채우기
for i in range(1, n + 1):
  for j in range(1, n + 1):
      if i == j:
          graph[i][j] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(c, graph[a][b]) # 노선이 하나가 아닐 수 있다.

# 최소값 업데이트
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("0", end=" ") # end 문자 추가해주는 것이 포인트
    else:
      print(graph[a][b], end=" ")
  print()


'''

# 인접행렬 값 기반으로 최소 비용으로 업데이트
for i in range(n+1):
  for j in range(n+1): 
    for k in range(n+1):
      if graph[i][k] != INF and graph[k][j] != INF:
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 업데이트
      else: continue

# 출력 형식부터 맞춰보
for i in range(1, n+1):
  print(graph[i][j] if graph[i][j] != INF else 0, sep=' ', end='\n')
  for j in range(1, n+1):
    if graph[i][j] != INF:
      print(graph[i][j] )
    else:
      print(0 )
      
  print("\n")


'''