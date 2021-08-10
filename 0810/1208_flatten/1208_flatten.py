import sys
sys.stdin = open('input.txt')

result = []
for _ in range(10):
    dump = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    while True:
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
        cnt += 1
        if cnt == dump:
            break
    result.append(max(lst) - min(lst))
for i in range(10):
    print('#{} {}'.format(i+1, result[i]))