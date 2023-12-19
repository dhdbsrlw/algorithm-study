import sys
import heapq
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())

dist = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def shortest_path(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        current_dist, cur = heapq.heappop(q)

        if current_dist > dist[cur]:
            continue

        for i in graph[cur]:
            cost = current_dist + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

shortest_path(k)

for i in range(1, v + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
