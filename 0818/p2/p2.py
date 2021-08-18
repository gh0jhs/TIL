import sys
sys.stdin = open('input.txt')

result = []
tc = int(input())
for _ in range(tc):
    top = -1
    gualho = input()
    stack = [''] * len(gualho)

    for i in gualho:
        top += 1
        stack[top] = i
        if i == ')':
            top -= 2
    if top == -1:
        result.append(1)
    else:
        result.append(-1)

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))