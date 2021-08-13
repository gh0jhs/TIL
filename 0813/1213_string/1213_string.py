import sys
sys.stdin = open('input.txt', encoding='UTF8')

result = []
for _ in range(10):
    t_number = input()
    search_string = input()
    sentence = input()

    N = len(sentence)
    M = len(search_string)
    i = 0
    j = 0
    cnt = 0
    while i != N:
        if search_string[j] == sentence[i]:
            j += 1
            if j == M:
                cnt += 1
                j = 0
        else:
            i -= j
            j = 0

        i += 1
    result.append(cnt)

for i in range(10):
    print('#{} {}'.format(i+1, result[i]))