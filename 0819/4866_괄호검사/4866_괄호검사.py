import sys
sys.stdin = open('input.txt')
#
result = []
tc = int(input())
for _ in range(tc):
    s = input()
    
    stack = []
    top = -1 # 스택 인덱스
    A = ['{', '}', '(', ')']

    for i in range(len(s)):
        if s[i] in A: # 괄호이면 스택에 추가하고 인덱스 1증가
            stack.append(s[i])
            top += 1
            if top >= 1:
                if (stack[top-1] == '{' and stack[top] == '}') or (stack[top-1] == '(' and stack[top] == ')'):
                    stack.pop()
                    stack.pop()
                    top -= 2

    if stack == []:
        result.append(1)
    else:
        result.append(0)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))