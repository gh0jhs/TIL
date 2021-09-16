import sys
sys.stdin = open('input.txt')
#
result = []
tc = int(input())
for _ in range(tc):
    cnt = 0
    x = 0
    r = 0
    temp = input()
    temp = temp.replace('()', 'r')
    for i in temp:
        if i == '(':
            x += 1
        elif i == 'r':
            cnt += x
        elif i == ')':
            cnt += 1
            x -= 1
    result.append(cnt)
for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))