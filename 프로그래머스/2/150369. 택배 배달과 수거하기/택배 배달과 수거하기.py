# 각 집마다 배달할 재활용 택배 상자의 개수
# 수거할 빈 재활용 택배 상자의 개수
# 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 '거리'
# 트럭은 택배상자를 최대 CAP 개 만큼 실을 수 있다.

# knapsack 문제? 그리디? 
# 결론적으로 그리디알고리즘을 사용하여야 한다. 
# 가장 멀리 위치한 것부터 처리하여야 한다.

def solution(cap, n, deliveries, pickups):
    
    # 역순으로 배열 뒤집기
    deliveries = deliveries[::-1] 
    pickups = pickups[::-1]
    result = 0
    
    del_needed = 0
    pick_needed = 0
    
    for i in range(n):
        del_needed += deliveries[i]
        pick_needed += pickups[i]
        
        # 아직 배달 또는 픽업할 것이 남아있는 경우
        while del_needed > 0 or pick_needed > 0:
            del_needed -= cap 
            pick_needed -= cap
            
            result += (n - i) * 2# 거리 추가
            
    return result
            
    