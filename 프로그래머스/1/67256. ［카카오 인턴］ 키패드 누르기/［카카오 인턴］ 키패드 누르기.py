'''
1,4,7 -> 무조건 L
3,6,9 -> 무조건 R
2,5,8,0 -> 더 가까운 손가락, 3으로 나눈 몫과 나머지로 거리 계산
curL, curR 변수 
'''

def solution(numbers, hand):
    
    result = []
    curL = 10
    curR = 12
    
    for num in numbers:
        
        if num == 0:
            num = 11
        
        if num == 1 or num == 4 or num == 7:
            result.append('L')
            curL = num
        elif num == 3 or num == 6 or num == 9:
            result.append('R')
            curR = num
        else:
            cmpL = abs((num - 1) // 3 - (curL - 1) // 3) + abs((num - 1) % 3 - (curL - 1) % 3) 
            cmpR = abs((num - 1) // 3 - (curR - 1) // 3) + abs((num - 1) % 3 - (curR - 1) % 3)
            
            if cmpL == cmpR:
                if hand == 'left':
                    result.append('L')
                    curL = num
                else:
                    result.append('R')
                    curR = num
                
            elif cmpL < cmpR:
                result.append('L')
                curL = num
            else: 
                result.append('R')
                curR = num
                
    result = ''.join(result)
    return result
            
    