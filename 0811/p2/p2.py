import sys
sys.stdin = open('input.txt')

lst = []
answer = []
tc = int(input())
for _ in range(tc):
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << 10):
        result = []
        for j in range(10):
            if i & (1 << j):
                result.append(lst[j])
                if sum(result) == 0:
                    cnt += 1
    if cnt == 0:
        answer.append(0)
    else:
        answer.append(1)
for i in range(tc):
    print('#{} {}'.format(i+1, answer[i]))