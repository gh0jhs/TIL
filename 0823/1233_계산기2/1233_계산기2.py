import sys
sys.stdin = open('input.txt')
#
for tc in range(1, 11):
    n = int(input())
    word = input()
    A = '+*'
    result = ''
    stack = []
    top = -1
    for i in word:
        if i not in A:
            result += i
        else:
            if top == -1:
                stack.append(i)
                top += 1
            elif i == '+':
                while top != -1:
                    result += stack.pop()
                    top -= 1
                stack.append(i)
                top += 1
            else:
                if stack[top] == '+':
                    stack.append(i)
                    top += 1
                else:
                    while stack[top] == '+':
                        result += stack.pop()
                        top -= 1
                        if top == -1:
                            break
                    stack.append(i)
                    top += 1
    while top != -1:
        result += stack.pop()
        top -= 1
    stack = []
    top = -1
    for i in result:
        if i not in A:
            stack.append(int(i))
        else:
            if i == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif i == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
    print('#{} {}'.format(tc, stack[0]))