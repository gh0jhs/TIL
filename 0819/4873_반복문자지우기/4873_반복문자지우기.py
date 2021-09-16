import sys
sys.stdin = open('input.txt')
#
result = [] # 결괏값
tc = int(input())
for _ in range(tc):
    s = input() # 스트링 입력받기
    
    stack = [s[0]] # 스택
    top = 0

    for i in range(1, len(s)):
        stack.append(s[i])
        top += 1
        if top >= 1: # 문자가 2개 있어야 비교 가능하므로 1보다 클 때
            if stack[top-1] == stack[top]:
                stack.pop()
                stack.pop()
                top -= 2

    result.append(len(stack))

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))
