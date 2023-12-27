# 여기 주석풀고 제출하면 출력 초과가 나온다
# import sys
# input = sys.stdin.readline

def stackLoop(text):
    stack = []
    for char in text:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False

while True:
    text = input()
    if text == '.': 
        break
    if stackLoop(list(text)):
        print('yes')
    else:
        print('no')