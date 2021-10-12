import sys
sys.stdin = open('input.txt')

# # 완전탐색
# T = int(input())
# for tc in range(1, T+1):
#     answer = 0
#     d1, m1, m3, y1 = map(int, input().split())
#     plan = list(map(int, input().split()))
#     fee = [0] * 12
#     for i in range(len(fee)):
#         fee[i] = min(d1 * plan[i], m1)
#     answer = sum(fee)
#     temp = answer
#
#     # 1
#     for i in range(len(fee)-2):
#         answer = min(answer, temp - (fee[i] + fee[i+1] + fee[i+2] - m3))
#     # 2
#     for i in range(len(fee)-5):
#         for j in range(i+3, len(fee)-2):
#             answer = min(answer, temp - (fee[i] + fee[i+1] + fee[i+2] + fee[j] + fee[j+1] + fee[j+2] - 2 * m3))
#     # 3
#     for i in range(len(fee)-8):
#         for j in range(i+3, len(fee)-5):
#             for k in range(j+3, len(fee)-2):
#                 answer = min(answer, temp - (fee[i] + fee[i + 1] + fee[i + 2] + fee[j] + fee[j + 1] + fee[j + 2] + fee[k] + fee[k + 1] + fee[k + 2] - 3 * m3))
#     # 4
#     answer = min(answer, 4*m3, y1)
#     print('#{} {}'.format(tc, answer))

# DP
T = int(input())
for tc in range(1, T+1):
    answer = 0
    d1, m1, m3, y1 = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12
    dp[0] = min(d1 * plan[0], m1)
    dp[1] = dp[0] + min(d1 * plan[1], m1)
    dp[2] = min(dp[1] + min(d1 * plan[2], m1), m3)
    for i in range(3, len(dp)):
        dp[i] = min(dp[i-1] + min(d1 * plan[i], m1), dp[i-3] + m3)

    answer = dp[-1]
    answer = min(answer, y1)
    print('#{} {}'.format(tc, answer))