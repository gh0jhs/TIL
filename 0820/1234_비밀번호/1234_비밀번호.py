import sys
sys.stdin = open('input.txt')

result = []
for _ in range(10):
    n, s = input().split()
    stack = []
    top = -1
    for i in range(len(s)):
        if stack == []:
            stack.append(s[i])
            top += 1
        else:
            stack.append(s[i])
            top += 1
            if stack[top-1] == stack[top]:
                stack.pop()
                stack.pop()
                top -= 2
    result.append(stack)

for i in range(10):
    print('#{} '.format(i+1), end='')
    for j in result[i]:
        print(j, end='')
    print()