import sys
sys.stdin = open('input.txt')
#
n = int(input())
result = []
for i in range(n):
    x = int(input())
    numbers = list(map(int, input().split()))
    min_val = numbers[0]
    max_val = numbers[0]
    # 최소값, 최대값
    for j in numbers:
        if min_val > j:
            min_val = j
        if max_val < j:
            max_val = j
    result.append(max_val - min_val)
for i in range(n):
    print('#{} {}'.format(i + 1, result[i]))