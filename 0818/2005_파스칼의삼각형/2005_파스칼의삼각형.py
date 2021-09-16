import sys
sys.stdin = input('open.txt')

#
arr = [0 for _ in range(10)] * 10
for i in range(10):
    for j in range(i+1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

result = []
lst = []
tc = int(input())
for _ in range(tc):
    lst.append(int(input()))

for i in range(len(lst)):
    print('#{}'.format(i+1))
    for j in range(lst[i]):
        for k in range(10):
            print(arr[j][k])

