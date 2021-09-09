n = int(input())
m = int(input())
A = [] ##
if m != 0:
    A = list(input().split())
min_temp = 123456789
for i in range(1000001):
    TF = True
    for j in A:
        if j in str(i):
            TF = False
            break
    if not TF:
        continue
    if min_temp > abs(n - i):
        min_temp = abs(n-i)
        min_i = i
if m == 10:
    print(abs(n-100))
else:
    print(min(min_temp + len(str(min_i)), abs(100-n)))