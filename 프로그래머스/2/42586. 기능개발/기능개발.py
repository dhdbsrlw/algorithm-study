from collections import deque

def solution(progresses, speeds):
    result = []
    queue_p = deque(progresses)
    queue_s = deque(speeds)
    
    queue_len = len(queue_p)
    day = 1    
    while queue_p:
        cum = 0
        while (queue_p[0] + (queue_s[0] * day) >= 100):
            cum += 1
            queue_p.popleft()
            queue_s.popleft()
            queue_len -= 1
            
            if queue_len == 0:
                break
    
        if cum != 0:
            result.append(cum)
        
        day += 1
    
    return result
    