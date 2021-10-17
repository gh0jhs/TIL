n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# dp
dp = [0 for _ in range(30)]
for i in range(len(arr)):
    if i + arr[i][0] <= n:
        dp[i] = arr[i][1]
    else:
        dp[i] = 0
for i in range(n-1, -1, -1):
    dp[i] = max(dp[i] + dp[i+arr[i][0]], dp[i+1])
print(dp[0]