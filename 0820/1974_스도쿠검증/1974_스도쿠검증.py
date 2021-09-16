import sys
sys.stdin = open('input.txt')
#
def test(arr):
    k1 = l1 = 0
    k2 = l2 = 3
    while k1 != 9:
        arr_t = []
        for i in range(k1, k2):
            for j in range(l1, l2):
                arr_t.append(arr[i][j])
        if [1,2,3,4,5,6,7,8,9] != sorted(arr_t):
            return 0
        l1 += 3
        l2 += 3
        if l1 == 9 and l2 == 12:
            k1 += 3
            k2 += 3
            l1 = 0
            l2 = 3

    # 합은 XXXXXXXXXXXX
    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            total += arr[i][j]
        if total != 45:
            return 0


    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            total += arr[j][i]
        if total != 45:
            return 0
    return 1


result = []
tc =int(input())
for _ in range(tc):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    result.append(test(arr))

for i in range(tc):
    print('#{} {}'.format(i+1, result[i]))