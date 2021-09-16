import sys
sys.stdin = open('input.txt')
#

#### 9 / 10 fail

T = int(input())
A = '+-*/.'
for tc in range(1, T+1):
    stack = []
    top = -1
    arr = list(input().split())
    for i in range(len(arr)):
        if arr[i] not in A:
            stack.append(int(arr[i]))
            top += 1
        else:
            if top >= 1:
                num2 = stack.pop()
                top -= 1
                num1 = stack.pop()
                top -= 1
                if arr[i] == '*':
                    x = num1 * num2
                    stack.append(int(x))
                    top += 1
                elif arr[i] == '/':
                    x = num1 / num2
                    stack.append(int(x))
                    top += 1
                elif arr[i] == '+':
                    x = num1 + num2
                    stack.append(int(x))
                    top += 1
                elif arr[i] == '-':
                    x = num1 - num2
                    stack.append(int(x))
                    top += 1
            else:
                if arr[i] == '.':
                    result = stack.pop()
                    top -=1
                else:
                    result = 'error'
                    break
    print('#{} {}'.format(tc, result))