from collections import deque

def solution(queue1, queue2):

    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    cnt = 0

    temp = s1 + s2
    # 합이 홀수일 경우
    if (temp % 2) != 0:
        return -1

    # 개선점: SUM 이나 LEN 을 한 번만 계산
    # 개선점: for 문으로 바꾼다.

    # 합이 짝수일 경우
    # while (len(q1) != 0 and len(q2) != 0):
    for i in range(300000): # 둘 중 어느 하나의 큐가 빌 때까지

        if (s1 == s2):
            return cnt

        elif (s1 > s2):
            num = q1.popleft()
            q2.append(num)
            s1 -= num
            s2 += num
            cnt += 1

        else:
            num = q2.popleft()
            q1.append(num)
            s1 += num
            s2 -= num
            cnt += 1

    return -1 
