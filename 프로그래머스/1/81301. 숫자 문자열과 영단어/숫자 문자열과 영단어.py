def solution(s):
    
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    char_list = list(s) # s 를 한 글자씩 분리
    
    temp = []
    # temp_len = 0
    result = []
    
    for c in char_list:
        # 숫자
        if c in num_list:
            if temp:
                word = ''.join(temp)
                if word in num_dict:
                    result.append(num_dict[word])
                temp.clear()
            result.append(c)
        
        # 문자
        else:
            temp.append(c)
            word = ''.join(temp)
            if word in num_dict:
                result.append(num_dict[word])
                temp.clear()
           
    # 아직 temp list 에 문자가 남아있을 경우
    if temp:
        word = ''.join(temp)
        if word in num_dict:
            result.append(num_dict[word])
                
                
    answer = int(''.join(result))
    return answer