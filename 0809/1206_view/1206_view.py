import sys
sys.stdin = open('input.txt')

n = 0
result = []
while n != 10:
    x = int(input())
    lst = []
    lst.append(list(map(int, input().split())))
    total = 0

    for i in lst:
        for idx in range(len(i)):
            if i[idx] == 0:
                continue
            # 왼쪽, 오른쪽 큰 값 결정
            if i[idx-2] > i[idx-1]:
                left = i[idx-2]
            else:
                left = i[idx-1]
            if i[idx+2] > i[idx+1]:
                right = i[idx+2]
            else:
                right = i[idx+1]
            if left > right:
                temp = left
            else:
                temp = right
            if left < i[idx] and right < i[idx]:
                total += i[idx] - temp
        result.append(total)
        n += 1
for i in range(1, 11):
    print('#{} {}'.format(i, result[i-1]))