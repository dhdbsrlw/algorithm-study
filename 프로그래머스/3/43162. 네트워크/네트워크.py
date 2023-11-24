# 2차원 배열, 일종의 adjacency matrix
# 연결되어 있는 경우 하나의 network 

# dfs (스택)
# 스택이 한 번 다 비워질 때마다 result 값 + 1
def solution(n, computers):
    
    result = 0
    stack = []
    linked = [0] * n # 컴퓨터의 연결 여부 
    
    for i in range(n):
        
        if linked[i] == 1:
            continue

        else:
            # 시작점 (new stack)
            stack.append(i)
            # linked[0] = 1

            # 깊이 탐색
            while stack:
                v = stack.pop() # 0
                if linked[v] == 0:
                    linked[v] = 1

                for idx, c in enumerate(computers[v]):
                    if v == idx: # 자기 자신
                        continue

                    if c == 1 and linked[idx] == 0:
                        stack.append(idx)
                        linked[idx] = 1
                        
            result += 1
        
    return result
        