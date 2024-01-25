# 접근 방법
# 1. ( 나 [ 는 스택에 삽입
# 2. ) 나 ] 는 pop 한 문자와 같지 않거나 없다면 false
# 3. 모든 문자 검사 후 스택에 괄호가 남아있다면 false
# 4. . 을 입력받을 때까지 반복

from collections import deque

while(1):

    str = input()

    if str == '.':
        break

    stack = deque()

    answer = True
    for s in str:

        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack.pop() != '(':
                answer = False
                break
        elif s == ']':
            if len(stack) == 0 or stack.pop() != '[':
                answer = False
                break

    if len(stack):
        answer = False

    if answer:
        print("yes")
    else:
        print("no")