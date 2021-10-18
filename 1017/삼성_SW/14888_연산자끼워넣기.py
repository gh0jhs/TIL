from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
temp = list(map(int, input().split()))
lst = []
for i in range(len(temp)):
    cnt = 0
    while temp[i] != cnt:
        if i == 0:
            lst.append('+')
            cnt += 1
        elif i == 1:
            lst.append('-')
            cnt += 1
        elif i == 2:
            lst.append('*')
            cnt += 1
        elif i == 3:
            lst.append('/')
            cnt += 1

A = list(permutations(lst))
A = list(set(A))
min_temp = 1000000000
max_temp = -1000000000

for i in range(len(A)):
    answer = arr[0]
    for j in range(len(A[i])):
        if A[i][j] == '+':
            answer += arr[j+1]
        elif A[i][j] == '-':
            answer -= arr[j+1]
        elif A[i][j] == '*':
            answer *= arr[j+1]
        elif A[i][j] == '/':
            if answer >= 0:
                answer //= arr[j+1]
            else:
                answer = -((-answer) // arr[j+1])
    if min_temp > answer:
        min_temp = answer
    if max_temp < answer:
        max_temp = answer
print(max_temp)
print(min_temp)