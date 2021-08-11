import sys
sys.stdin = open('input.txt')

answer = []
for _ in range(10):
    result = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range (100)]
    total_x_1 = 0
    total_x_2 = 0
    for i in range(100):
        total_row = 0
        total_col = 0
        for j in range(100):
            total_row += arr[i][j]
            total_col += arr[j][i]
            if i == j:
                total_x_1 += arr[i][j]
            if i + j == 99:
                total_x_2 += arr[i][j]
        result.append(total_row)
        result.append(total_col)
    result.append(total_x_1)
    result.append(total_x_2)
    answer.append(max(result))
for i in range(10):
    print('#{} {}'.format(i+1, answer[i]))

#    # 행 연산 더하기
#     for i in range(100):
#         total = 0
#         for j in range(100):
#             total += arr[i][j]
#         result.append(total)
#     # 열 연산 더하기
#     for i in range(100):
#         total = 0
#         for j in range(100):
#             total += arr[j][i]
#         result.append(total)
#
#     total = 0
#     # 대각선
#     for i in range(100):
#         for j in range(100):
#             if i == j:
#                 total += arr[i][j]
#     result.append(total)
#
#     total = 0
#     # 반대 대각선
#     for i in range(100):
#         for j in range(100):
#             if i + j == 99:
#                 total += arr[i][j]
#     result.append(total)
#     answer.append(max(result))
# for i in range(10):
#     print('#{} {}'.format(i+1, answer[i]))

