import sys
sys.stdin = open('input.txt')
#
result = []
tc = int(input())
for _ in range(tc):
    arr = []
    arr1 = []
    arr2 = []
    arr3 = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(len(arr)):
        for j in range(len(arr)-1, -1, -1):
            arr1.append(str(arr[j][i]))

    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, -1, -1):
            arr2.append(str(arr[i][j]))

    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)):
            arr3.append(str(arr[j][i]))
    lst = []
    k = 0
    while True:
        x1 = ''.join(arr1[k:k+n])
        x2 = ''.join(arr2[k:k+n])
        x3 = ''.join(arr3[k:k+n])
        str1 = x1 + ' ' + x2 + ' ' + x3
        lst.append(str1)
        k += n
        if k == len(arr1):
            break
    result.append(lst)

for i in range(tc):
    print('#{}'.format(i+1))
    for j in range(len(result[i])):
        print('{}'.format(result[i][j]))