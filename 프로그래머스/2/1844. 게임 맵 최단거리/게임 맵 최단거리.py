# 0 은 벽이 있는 자리, 1은 벽이 없는 자리
# bfs , 최단 거리 문제에는 dfs 보다 bfs 를 사용한다.
from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    
    queue = deque([[0, 0]]) 
    # print(queue)
    # visited = [[0] * n for _ in range(m)] 
    # dist = [[0] * n for _ in range(m)] 
    
    visited = [[0] * m for _ in range(n)] 
    dist = [[0] * m for _ in range(n)] 
    
    
    visited[0][0] = 1
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        # print((x, y))
        
        dx = [-1, 1, 0, 0] # 좌우
        dy = [0, 0, -1, 1] # 상하
        
        for i in range(4): # 상하좌우 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0: # 범위 내, 방문한 적 없는 노드
                if maps[nx][ny] == 0: # 벽이 존재하는 경우
                    visited[nx][ny] = 1
                    continue # 갈 수 없는 길
                
                else:
                    # 이 단계에서 죄다 append 를 하면 안된다. 네 방향 중 하나 선택.
                    queue.append([nx, ny]) 
                    visited[nx][ny] = 1
                    dist[nx][ny] = max(dist[nx][ny], dist[x][y] + 1)
                    
    # print(dist)
    if dist[n-1][m-1] == 0:
        return -1
    
    else: return dist[n-1][m-1]
   