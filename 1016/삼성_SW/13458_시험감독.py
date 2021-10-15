n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for i in range(len(a)):
    answer += 1
    a[i] -= b
    if a[i] <= 0:
        continue
    if a[i] % c == 0:
        answer += a[i] / c
    else:
        answer += (a[i] // c) + 1
print(int(answer))