import sys
sys.stdin = open('input.txt')

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
tc = int(input())

result = []
for _ in range(tc):
    tc_number, length = input().split()
    length = int(length)
    lst = list(input().split())
    for i in range(length):
        for j in range(i+1, length):
            if numbers.index(lst[i]) > numbers.index(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    result.append(lst)

for i in range(tc):
    print('#{}'.format(i+1))
    for j in result[i]:
        print(j, end = ' ')