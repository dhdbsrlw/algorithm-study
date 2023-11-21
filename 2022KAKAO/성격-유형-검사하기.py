def solution(survey, choices):

    type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    # 점수 축적
    for i in range(len(survey)):

        s = survey[i]
        c = choices[i]

        temp = c - 4  

        if (temp == 0):
            continue
        elif (temp > 0):
            score[s[1]] = score[s[1]] + temp # 동의 관련 선택지
        else:
            score[s[0]] = score[s[0]] - temp # 비동의 관련 선택지

    # 점수비교
    answer_list = [] # append 형태
    for i in range(4): 
        i = i * 2
        v1 = type[i]
        v2 = type[i+1]
        if (score[v1] == score[v2]) or (score[v1] > score[v2]):
            answer_list.append(v1)
        else:
            answer_list.append(v2)

    answer = ''.join(answer_list)
    return answer
