import sys
sys.stdin = open('input.txt')
#
result = []
for _ in range(10):
    test_number = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    x = arr[99].index(2)
    i = 98
    right = 0
    left = 0
    while i != 0:
            if x+1 <= 99 and arr[i][x+1] == 1 and left == 0:
                right = 1
                x += 1
                if x == 99:
                    right = 0
                elif arr[i][x+1] == 0:
                    right = 0
            elif x-1 >= 0 and arr[i][x-1] == 1 and right == 0:
                left = 1
                x -= 1
                if x == 0:
                    left = 0
                elif arr[i][x-1] == 0:
                    left = 0
            if left == 0 and right == 0:
                i -= 1
    result.append(x)
for i in range(10):
    print('#{} {}'.format(i+1, result[i]))