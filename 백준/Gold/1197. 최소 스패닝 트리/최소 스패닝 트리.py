import sys
import heapq
# input = sys.stdin.readline  # IDE에서 실행할 경우 주석 처리

v, e = map(int, input().split())  # input()으로 변경
visited = [False] * (v+1)
elist = [[] for _ in range(v+1)]
heap = [[0,1]]

for _ in range(e):
    s, e, w = map(int, input().split())  # input().split()으로 변경
    elist[s].append([w,e])
    elist[e].append([w,s])

ans = 0
cnt = 0

while heap:
    if cnt == v:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        ans += w
        cnt += 1
        for i in elist[s]:
            heapq.heappush(heap, i)

print(ans)
